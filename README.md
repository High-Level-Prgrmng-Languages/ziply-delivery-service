
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
