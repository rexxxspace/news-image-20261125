// Entry program for the make.fun news-image-20261125 contest.
//
// The artwork is entry.png, sitting next to this file: a newspaper front
// page covering Wednesday, 25 November 2026. All this program does is
// deliver that artwork to the location the grader reads - entry.png
// inside the output folder, which is /output in the grading sandbox or
// whatever MAKEFUN_OUTPUT_DIR points at during a local dry run.
//
// Because the delivery is a straight byte-for-byte copy of a committed
// file, repeated runs always land on identical output.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const folder = dirname(fileURLToPath(import.meta.url));
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

// The output folder is not guaranteed to exist yet (a fresh local dry run
// points MAKEFUN_OUTPUT_DIR at a folder nobody made), and copyFileSync
// throws on a missing destination directory - so create it first.
mkdirSync(targetDir, { recursive: true });

copyFileSync(join(folder, "entry.png"), join(targetDir, "entry.png"));
