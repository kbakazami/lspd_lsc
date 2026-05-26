import { defineConfig } from 'sanity';
import { structureTool } from 'sanity/structure';
import { visionTool } from '@sanity/vision';
import recruitmentEvent from './sanity/schemas/recruitmentEvent';
import author from './sanity/schemas/author';
import post from './sanity/schemas/post';
import rank from './sanity/schemas/rank';
import division from './sanity/schemas/division';

export default defineConfig({
  name: 'lspd-studio',
  title: 'LSPD — lsh-rp',
  projectId: 'ybq4sq6q',
  dataset: 'production',
  plugins: [structureTool(), visionTool()],
  schema: { types: [recruitmentEvent, author, post, rank, division] },
});