// Create indexes for optimal query performance
db.pages.createIndex({ "owner_id": 1, "updated_at": -1 });
db.pages.createIndex({ "url": 1 }, { unique: true });
db.pages.createIndex({ "metadata.tags": 1 });

db.parcels.createIndex({ "tracking_number": 1 }, { unique: true });
db.parcels.createIndex({ "recipient.address.zip": 1 });
db.parcels.createIndex({ "current_status": 1, "created_at": -1 });
db.parcels.createIndex({ "status_history.timestamp": -1 });