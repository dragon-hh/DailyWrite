import fs from "node:fs";
import path from "node:path";

const suiteRoot = path.resolve(import.meta.dirname, "..");
const skillsRoot = path.resolve(suiteRoot, "..");
const dirs = fs.readdirSync(skillsRoot, { withFileTypes: true })
  .filter((entry) => entry.isDirectory() && entry.name.startsWith("dbs"))
  .map((entry) => entry.name)
  .sort();

const errors = [];
const warnings = [];
const requiredShared = "operating-contract.md";
for (const name of dirs) {
  const skillPath = path.join(skillsRoot, name, "SKILL.md");
  if (!fs.existsSync(skillPath)) {
    errors.push(`${name}: missing SKILL.md`);
    continue;
  }
  const text = fs.readFileSync(skillPath, "utf8");
  const frontmatter = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!frontmatter) {
    errors.push(`${name}: missing YAML frontmatter`);
    continue;
  }
  const nameMatch = frontmatter[1].match(/^name:\s*([^\r\n]+)/m);
  const descriptionMatch = frontmatter[1].match(/^description:\s*([\s\S]*)/m);
  if (!nameMatch || nameMatch[1].trim() !== name) {
    errors.push(`${name}: frontmatter name does not match directory`);
  }
  if (!descriptionMatch || descriptionMatch[1].trim().length < 12) {
    errors.push(`${name}: description is missing or too short`);
  }
  const requiredLink = name === "dbs"
    ? "references/operating-contract.md"
    : "../dbs/references/operating-contract.md";
  if (!text.includes(requiredLink)) {
    errors.push(`${name}: missing shared contract link ${requiredLink}`);
  }
  if (text.includes("知识库/Skill知识包/")) {
    warnings.push(`${name}: contains a legacy knowledge-pack reference; verify it exists before using it`);
  }
}
const registryPath = path.join(suiteRoot, "references", "registry.md");
if (fs.existsSync(registryPath)) {
  const registryText = fs.readFileSync(registryPath, "utf8");
  for (const name of dirs.filter((entry) => entry !== "dbs")) {
    if (!registryText.includes(`\`${name}\``)) errors.push(`registry: missing ${name}`);
  }
}
for (const required of [
  path.join(suiteRoot, "references", "operating-contract.md"),
  path.join(suiteRoot, "references", "registry.md"),
]) {
  if (!fs.existsSync(required)) errors.push(`missing shared resource: ${required}`);
}

console.log(`dbs suite: ${dirs.length} skills checked`);
for (const warning of warnings) console.log(`WARN ${warning}`);
if (errors.length) {
  for (const error of errors) console.error(`ERROR ${error}`);
  process.exitCode = 1;
} else {
  console.log("OK: frontmatter, shared contract links, and required resources are valid");
}



