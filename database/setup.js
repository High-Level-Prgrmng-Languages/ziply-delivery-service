require('dotenv').config();
const { MongoClient } = require('mongodb');

const uri = process.env.MONGODB_URI;
const dbName = process.env.DB_NAME || 'delivery_service';

async function createDatabaseWithSample() {
  if (!uri) {
    throw new Error('MONGODB_URI not found in environment variables');
  }

  try {
    const client = new MongoClient(uri);
    await client.connect();
    const db = client.db(dbName);
    console.log('Connected to MongoDB successfully');

    // Sample parcel data
    const sampleParcel = {
      tracking_number: "TRK123456789",
      sender: {
        name: "John Doe",
        address: {
          street: "123 Main St",
          city: "New York",
          zip: "10001"
        }
      },
      recipient: {
        name: "Jyot Harshadkumar Bhavsar",
        address: {
          street: "Humber ",
          city: "Toronto",
          zip: "M1C 1A4"
        }
      },
      current_status: "in_transit",
      created_at: new Date(),
      estimated_delivery: new Date(Date.now() + 3 * 24 * 60 * 60 * 1000)
    };

    // Insert sample data
    await db.collection('parcels').insertOne(sampleParcel);
    console.log('Sample parcel inserted successfully');

    await client.close();

  } catch (error) {
    console.error('Database setup error:', error);
    process.exit(1);
  }
}

createDatabaseWithSample();
