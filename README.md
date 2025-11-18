<<<<<<< HEAD
## Database Design

### NoSQL Schema
Our system uses MongoDB for flexible document storage optimized for:
- **Page Data**: Denormalized documents with embedded metadata and analytics
- **Parcel Tracking**: Event-sourced status history with current state optimization

### Key Design Decisions
- Embedded status history in parcels for atomic updates
- Separate collections for different access patterns
- Strategic indexing for common query patterns

See `/database/schemas/` for detailed schema definitions.
=======
# Delivery Service Website

Tracks parcels and bulk parcel information for businesses.

# Primary Services
Description of the primary service this website provides is in two categories: 

1. Company Use
2. Customer Use

## Company Use
Companies can store inventory information and parcel information allowing them to track the progress through scanning bar codes and updating parcel information such as the status, additional delivery instructions, the content, price. Inventory information tells the companies what parcels are waiting for shipment and why. 

Companies require a account to log and track this information.

## Customer Use
Customers can receive parcel information via a delivery id and search up the progress on this site. 
Customer may optionally use an account to track and recieve updates through email.

## File Structure

- **`src/`**: Python Source Files 
>>>>>>> main
