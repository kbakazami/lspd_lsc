export type ArticleCategory =
  | 'Communiqué officiel'
  | 'Ressources humaines'
  | 'Avis au public'
  | 'Opérations'
  | 'Vie du département';

export type BodyBlock =
  | { type: 'paragraph'; content: string }
  | { type: 'heading'; content: string }
  | { type: 'quote'; content: string };

export interface NewsArticle {
  slug: string;
  title: string;
  excerpt: string;
  category: ArticleCategory;
  date: string;
  isoDate: string;
  author: { name: string; rank: string };
  readTime: number;
  body: BodyBlock[];
  tags: string[];
}

export const ALL_CATEGORIES: ArticleCategory[] = [
  'Communiqué officiel',
  'Ressources humaines',
  'Avis au public',
  'Opérations',
  'Vie du département',
];

export const mockNews: NewsArticle[] = [
  {
    slug: 'operation-vague-bleue-bilan',
    title: "Point presse — Opération « Vague Bleue » : bilan et résultats",
    excerpt:
      "Suite à dix jours d'opérations intensives dans les quartiers de Chamberlain Hills et Strawberry, le LSPD dresse un bilan positif avec 47 interpellations et la saisie de 12 kg de stupéfiants.",
    category: 'Communiqué officiel',
    date: '14 mai 2026',
    isoDate: '2026-05-14',
    author: { name: 'James Calloway', rank: 'Commissaire Divisionnaire' },
    readTime: 4,
    body: [
      {
        type: 'paragraph',
        content:
          "Le Los Santos Police Department est en mesure de communiquer aujourd'hui les résultats définitifs de l'opération « Vague Bleue », conduite entre le 4 et le 14 mai 2026 dans les quartiers de Chamberlain Hills, Strawberry et Davis, identifiés comme foyers majeurs de trafic de stupéfiants à l'issue d'une enquête de six mois menée par le Bureau des Détectives.",
      },
      { type: 'heading', content: 'Bilan opérationnel' },
      {
        type: 'paragraph',
        content:
          "47 individus ont été interpellés au cours de l'opération, dont 12 pour association de malfaiteurs en lien avec le trafic de stupéfiants. 12,4 kg de substances illicites ont été saisis, ainsi que 8 armes à feu non déclarées et un véhicule utilisé à des fins criminelles.",
      },
      {
        type: 'paragraph',
        content:
          "Les équipes mobilisées comprenaient des agents en tenue, des inspecteurs du Bureau des Détectives ainsi qu'une équipe de surveillance héliportée de l'Air Support Unit. L'ensemble des personnels a fait preuve d'un professionnalisme exemplaire tout au long de la mission.",
      },
      { type: 'heading', content: 'Poursuites judiciaires' },
      {
        type: 'paragraph',
        content:
          "Le dossier d'accusation a été transmis au Parquet de l'État de San Andreas. Le LSPD collabore pleinement avec le Procureur de la République pour s'assurer que les prévenus répondent de leurs actes devant les juridictions compétentes.",
      },
      {
        type: 'quote',
        content:
          "Cette opération démontre la capacité de notre département à conduire des enquêtes de longue durée et à frapper de manière décisive les structures criminelles organisées qui menacent la paix de nos quartiers.",
      },
      {
        type: 'paragraph',
        content:
          "Le département tient à remercier les citoyens qui ont contribué à cette réussite par leurs signalements et leur coopération avec les forces de l'ordre.",
      },
    ],
    tags: ['opération', 'stupéfiants', 'Chamberlain Hills'],
  },
  {
    slug: 'promotions-printemps-2026',
    title: "Promotions au sein du département — session du printemps 2026",
    excerpt:
      "Le Commissaire Général porte à la connaissance du public les promotions accordées lors de la cérémonie du 8 mai. Quatre officiers sont promus au grade de Sergent à la suite de leurs résultats exceptionnels.",
    category: 'Ressources humaines',
    date: '8 mai 2026',
    isoDate: '2026-05-08',
    author: { name: 'Sandra Morales', rank: 'Directrice des Ressources Humaines' },
    readTime: 3,
    body: [
      {
        type: 'paragraph',
        content:
          "Le Los Santos Police Department a procédé, le vendredi 8 mai 2026, à la cérémonie de promotion trimestrielle au cours de laquelle le Commissaire Général a remis leurs galons à quatre officiers méritants, en présence du personnel du département et de représentants de la mairie de Los Santos.",
      },
      { type: 'heading', content: 'Officiers promus au grade de Sergent' },
      {
        type: 'paragraph',
        content:
          "Les officiers Kevin Bradshaw, Maria Chen, Devon Pierce et Rosa Gutierrez accèdent au grade de Sergent à compter du 8 mai 2026. Ces promotions récompensent des parcours exemplaires marqués par un taux d'élucidation supérieur à la moyenne départementale, une évaluation comportementale positive et la validation de l'ensemble des formations réglementaires.",
      },
      {
        type: 'quote',
        content:
          "La promotion n'est pas une récompense du passé, c'est une confiance accordée pour l'avenir. Je félicite chacun de ces officiers et compte sur eux pour incarner les valeurs du LSPD auprès de leurs équipes.",
      },
      {
        type: 'paragraph',
        content:
          "Le département tient également à distinguer l'Officier Première Classe James Huang, dont le dossier a été retenu pour la prochaine session de promotion au grade de Sergent, sous réserve de validation de sa dernière certification de tir.",
      },
    ],
    tags: ['promotions', 'ressources humaines', 'cérémonie'],
  },
  {
    slug: 'fermeture-accueil-administratif',
    title: "Fermeture temporaire de l'accueil administratif — travaux de rénovation",
    excerpt:
      "Le LSPD informe la population que le guichet administratif du commissariat central de Mission Row sera fermé du 5 au 19 mai dans le cadre de travaux de rénovation. Les services restent accessibles en ligne.",
    category: 'Avis au public',
    date: '2 mai 2026',
    isoDate: '2026-05-02',
    author: { name: "Patricia O'Brien", rank: 'Secrétaire Générale' },
    readTime: 2,
    body: [
      {
        type: 'paragraph',
        content:
          "Le Los Santos Police Department porte à la connaissance de la population que l'accueil administratif du commissariat central situé au 7 Mission Row sera fermé au public du lundi 5 mai au dimanche 19 mai 2026, dans le cadre de travaux de rénovation et de mise aux normes des locaux.",
      },
      { type: 'heading', content: 'Services maintenus pendant la fermeture' },
      {
        type: 'paragraph',
        content:
          "Les services administratifs restent accessibles par voie électronique via le formulaire de contact disponible sur le présent site. Les demandes de documents officiels (certificats, rapports d'incidents) peuvent être formulées par courrier postal à l'adresse du commissariat. Les urgences sont à composer au 911.",
      },
      {
        type: 'paragraph',
        content:
          "Le commissariat de Sandy Shores reste ouvert et prend en charge les administrés qui nécessitent un rendez-vous physique urgent. Des créneaux de permanence sont disponibles le mardi et le jeudi de 9h à 12h.",
      },
      { type: 'heading', content: 'Reprise du service normal' },
      {
        type: 'paragraph',
        content:
          "L'accueil administratif rouvrira ses portes le lundi 20 mai 2026 avec des horaires élargis (8h–18h) pendant une semaine afin d'absorber les demandes en attente. Le LSPD s'excuse des désagréments occasionnés et remercie la population pour sa compréhension.",
      },
    ],
    tags: ['administration', 'Mission Row', 'travaux'],
  },
  {
    slug: 'arrestation-cellule-maze-bank',
    title: "Arrestation majeure — démantèlement d'une cellule de blanchiment dans le quartier financier",
    excerpt:
      "Après quatre mois d'enquête, le Bureau des Détectives procède à l'interpellation d'un individu soupçonné de diriger un réseau de blanchiment d'argent opérant depuis plusieurs adresses du quartier de Maze Bank.",
    category: 'Communiqué officiel',
    date: '28 avril 2026',
    isoDate: '2026-04-28',
    author: { name: 'Frank Okafor', rank: 'Inspecteur en Chef' },
    readTime: 5,
    body: [
      {
        type: 'paragraph',
        content:
          "À l'issue d'une enquête de quatre mois conduite conjointement par le Bureau des Détectives du LSPD et l'Unité Financière du Parquet de San Andreas, les forces de l'ordre ont procédé le jeudi 28 avril 2026 à l'arrestation d'un individu de 38 ans, soupçonné d'être à la tête d'un réseau de blanchiment d'argent dont les ramifications s'étendent à plusieurs établissements commerciaux du quartier financier de Los Santos.",
      },
      { type: 'heading', content: "Déroulement de l'opération" },
      {
        type: 'paragraph',
        content:
          "L'interpellation a eu lieu à l'aube dans un appartement de la Maze Bank Tower. Trois autres suspects ont été appréhendés simultanément dans deux adresses distinctes de Rockford Hills. Aucun incident majeur n'est à déplorer lors des opérations, qui se sont déroulées conformément aux protocoles d'intervention du LSPD.",
      },
      {
        type: 'paragraph',
        content:
          "Les perquisitions menées concomitamment ont permis de saisir documents comptables, supports numériques et numéraires pour un montant estimé à 1,2 million de dollars. L'ensemble du matériel est actuellement en cours d'analyse par les experts de l'unité légale du département.",
      },
      {
        type: 'quote',
        content:
          "La criminalité en col blanc ne bénéficie d'aucune impunité dans notre ville. Le LSPD dispose des ressources et de la détermination nécessaires pour traquer ces infractions aussi rigoureusement que tout autre forme de criminalité.",
      },
      {
        type: 'paragraph',
        content:
          "Les quatre suspects ont été présentés au magistrat instructeur dans les vingt-quatre heures suivant leur arrestation. La procédure judiciaire suit son cours. Le LSPD ne fera aucun commentaire supplémentaire dans l'intérêt de l'enquête en cours.",
      },
    ],
    tags: ['arrestation', 'blanchiment', 'Maze Bank', 'Bureau des Détectives'],
  },
  {
    slug: 'inauguration-centre-formation-2026',
    title: "Inauguration du nouveau Centre de Formation et d'Entraînement du LSPD",
    excerpt:
      "Le département inaugure ses nouvelles installations situées à La Mesa, dotées d'un pas de tir modernisé, d'un parcours de conduite tactique et d'un espace de simulation d'intervention.",
    category: 'Vie du département',
    date: '18 avril 2026',
    isoDate: '2026-04-18',
    author: { name: 'Sandra Morales', rank: 'Directrice des Ressources Humaines' },
    readTime: 3,
    body: [
      {
        type: 'paragraph',
        content:
          "Le Los Santos Police Department a inauguré le vendredi 18 avril 2026 son nouveau Centre de Formation et d'Entraînement (CFE), situé dans le quartier de La Mesa. Ces installations, dont la construction a mobilisé un investissement budgétaire significatif, ont été conçues pour répondre aux besoins de formation continue de l'ensemble des effectifs du département.",
      },
      { type: 'heading', content: 'Équipements et infrastructure' },
      {
        type: 'paragraph',
        content:
          "Le CFE comprend un pas de tir de 25 mètres homologué pour l'entraînement au pistolet et au fusil de précision, un parcours de conduite tactique incluant des zones d'évitement dynamique, ainsi qu'une salle de simulation d'intervention en environnement confiné. Des salles de formation théorique équipées de matériel audiovisuel complètent le dispositif.",
      },
      {
        type: 'paragraph',
        content:
          "Les recrues des prochaines promotions d'académie bénéficieront de l'ensemble de ces installations dans le cadre du programme de formation initiale de seize semaines. Les officiers en service bénéficieront d'un accès prioritaire les fins de semaine pour les séances de maintien des acquis.",
      },
      {
        type: 'quote',
        content:
          "Un officier bien formé est un officier efficace et en sécurité. Ce centre est un investissement dans la qualité de notre service et dans la protection de notre personnel.",
      },
    ],
    tags: ['formation', 'La Mesa', 'infrastructure'],
  },
  {
    slug: 'avis-recherche-vehicule-chamberlain',
    title: "Avis de recherche — véhicule utilitaire soustrait dans le secteur de Chamberlain Hills",
    excerpt:
      "Le LSPD demande la coopération de la population pour localiser un véhicule utilitaire de marque Vapid, immatriculé en San Andreas, dérobé dans la nuit du 25 au 26 avril dans le secteur de Chamberlain Hills.",
    category: 'Avis au public',
    date: '26 avril 2026',
    isoDate: '2026-04-26',
    author: { name: 'Thomas Erikson', rank: 'Sergent de Permanence' },
    readTime: 2,
    body: [
      {
        type: 'paragraph',
        content:
          "Le Los Santos Police Department porte à la connaissance de la population la disparition d'un véhicule utilitaire léger de marque Vapid, de couleur blanche, immatriculé au nom d'une société de messagerie de Los Santos. Le véhicule a été dérobé dans la nuit du dimanche 25 au lundi 26 avril dans la rue Jamestown Street, quartier de Chamberlain Hills.",
      },
      { type: 'heading', content: 'Signalement' },
      {
        type: 'paragraph',
        content:
          "Toute personne ayant aperçu ce véhicule est priée de contacter le central du LSPD en composant le 911 ou de déposer un signalement via le formulaire en ligne disponible sur ce site. Le LSPD rappelle à la population de ne pas tenter d'intervenir par elle-même et de ne pas approcher le véhicule si celui-ci est localisé.",
      },
      {
        type: 'paragraph',
        content:
          "Une enquête est en cours. Des équipes de patrouille ont été affectées au secteur pour accroître la surveillance du périmètre. Le LSPD remercie la population pour sa vigilance et sa coopération.",
      },
    ],
    tags: ['avis de recherche', 'vol de véhicule', 'Chamberlain Hills'],
  },
  {
    slug: 'bilan-criminalite-2025',
    title: "Rapport annuel 2025 — évolution de la criminalité dans le comté de Los Santos",
    excerpt:
      "Le département publie son rapport statistique annuel. Les indicateurs font état d'une réduction de 11 % des infractions violentes par rapport à 2024, malgré une hausse des délits routiers.",
    category: 'Communiqué officiel',
    date: '10 avril 2026',
    isoDate: '2026-04-10',
    author: { name: 'James Calloway', rank: 'Commissaire Divisionnaire' },
    readTime: 6,
    body: [
      {
        type: 'paragraph',
        content:
          "Conformément à ses obligations de transparence, le Los Santos Police Department publie ce jour son rapport annuel sur l'évolution de la criminalité dans le comté de Los Santos pour l'exercice 2025. Ce document, établi par le service statistique du département, est disponible dans son intégralité auprès du secrétariat administratif.",
      },
      { type: 'heading', content: 'Faits saillants — infractions violentes' },
      {
        type: 'paragraph',
        content:
          "Le taux d'infractions violentes (agression, braquage, homicide) accuse une baisse de 11 % par rapport à l'exercice 2024, résultat que le département attribue au renforcement des effectifs de patrouille dans les zones sensibles et au déploiement des unités de proximité depuis le second semestre 2024.",
      },
      { type: 'heading', content: 'Délits routiers en hausse' },
      {
        type: 'paragraph',
        content:
          "À rebours de cette tendance positive, les infractions routières graves (conduite sous influence, excès de vitesse extrêmes, défaut d'assurance) enregistrent une augmentation de 8 % sur l'ensemble du réseau routier du comté. La Highway Patrol Unit a vu ses effectifs renforcés en début d'année 2026 pour répondre à cette problématique.",
      },
      {
        type: 'quote',
        content:
          "La baisse des violences confirme que notre stratégie de présence terrain porte ses fruits. La route reste un combat quotidien et nous redoublons d'efforts pour y maintenir la sécurité.",
      },
      {
        type: 'paragraph',
        content:
          "Le rapport complet, incluant les tableaux de bord par quartier et les données comparatives sur cinq ans, est téléchargeable auprès du secrétariat du département sur rendez-vous.",
      },
    ],
    tags: ['rapport annuel', 'statistiques', 'criminalité'],
  },
  {
    slug: 'appel-temoins-mission-row',
    title: "Appel à témoins — incident survenu le 3 avril devant le commissariat central",
    excerpt:
      "Le LSPD recherche des témoins d'une altercation ayant eu lieu le 3 avril 2026 en début de soirée sur le parvis du commissariat de Mission Row. Toute information est susceptible de contribuer à l'enquête.",
    category: 'Avis au public',
    date: '5 avril 2026',
    isoDate: '2026-04-05',
    author: { name: 'Thomas Erikson', rank: 'Sergent de Permanence' },
    readTime: 2,
    body: [
      {
        type: 'paragraph',
        content:
          "Le Los Santos Police Department lance un appel à témoins concernant un incident survenu le vendredi 3 avril 2026 entre 19h30 et 20h15 sur le parvis du commissariat central de Mission Row. Une altercation impliquant deux individus a conduit à l'intervention d'agents de faction, et les circonstances précédant cet incident font l'objet d'une enquête.",
      },
      { type: 'heading', content: 'Comment témoigner' },
      {
        type: 'paragraph',
        content:
          "Toute personne présente à proximité des lieux entre les heures mentionnées est invitée à se manifester auprès du LSPD. Les témoignages peuvent être transmis de manière confidentielle via le formulaire de contact de ce site, ou en se présentant directement au commissariat. L'identité des témoins est protégée par la loi.",
      },
      {
        type: 'paragraph',
        content:
          "Le LSPD rappelle que tout témoignage, même partiel, peut s'avérer déterminant dans le cadre d'une enquête. Nous remercions la population pour sa coopération habituelle.",
      },
    ],
    tags: ['appel à témoins', 'Mission Row', 'incident'],
  },
];
