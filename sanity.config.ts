import { defineConfig } from 'sanity';
import { structureTool } from 'sanity/structure';
import { visionTool } from '@sanity/vision';
import recruitmentEvent from './sanity/schemas/recruitmentEvent';
import recruitmentSettings from './sanity/schemas/recruitmentSettings';
import author from './sanity/schemas/author';
import post from './sanity/schemas/post';
import rank from './sanity/schemas/rank';
import division from './sanity/schemas/division';

/** Types édités via un document unique, sortis de la liste générique. */
const SINGLETONS = ['recruitmentSettings'];

export default defineConfig({
  name: 'lspd-studio',
  title: 'LSPD — lsh-rp',
  projectId: 'ybq4sq6q',
  dataset: 'production',
  plugins: [
    structureTool({
      structure: (S) =>
        S.list()
          .title('Contenu')
          .items([
            S.listItem()
              .title('Paramètres du recrutement')
              .id('recruitmentSettings')
              .child(
                S.document()
                  .schemaType('recruitmentSettings')
                  .documentId('recruitmentSettings')
                  .title('Paramètres du recrutement'),
              ),
            S.divider(),
            ...S.documentTypeListItems().filter(
              (item) => !SINGLETONS.includes(item.getId() ?? ''),
            ),
          ]),
    }),
    visionTool(),
  ],
  schema: {
    types: [recruitmentEvent, recruitmentSettings, author, post, rank, division],
    templates: (templates) =>
      templates.filter(({ schemaType }) => !SINGLETONS.includes(schemaType)),
  },
});
