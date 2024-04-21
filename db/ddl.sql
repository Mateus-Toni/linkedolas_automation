CREATE TABLE leads (
    lead_id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    url_lead VARCHAR(250),
    cellphone VARCHAR(100)
);

CREATE TABLE campaigns (
    id_campaign SERIAL PRIMARY KEY,
    name_campaign VARCHAR(255)
);

CREATE TABLE tasks (
    id_task SERIAL PRIMARY KEY,
    name_task VARCHAR(255)
);

CREATE TABLE campaign_tasks (
    id_campaign_task SERIAL PRIMARY KEY,
    id_campaign INT,
    id_task INT,
    order_number INT,
    FOREIGN KEY (id_campaign) REFERENCES campaigns(id_campaign),
    FOREIGN KEY (id_task) REFERENCES tasks(id_task)
);

CREATE TABLE leads_campaign (
    lead_id INT,
    campaign_id INT,
    PRIMARY KEY (lead_id, campaign_id),
    FOREIGN KEY (lead_id) REFERENCES leads(lead_id),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id_campaign)
);

CREATE TABLE leads_campaign (
    lead_id INT,
    campaign_id INT,
    PRIMARY KEY (lead_id, campaign_id),
    FOREIGN KEY (lead_id) REFERENCES leads(lead_id),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id_campaign)
);
