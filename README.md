# FastAPI and SQlite
FastAPI SQlite 데이터 공유 테스트

```mermaid
%%{
  init: {
    "theme": "dark",
    "flowchart": {      
      "_defaultRenderer": "elk"
    }    
  }
}%%
flowchart TB
subgraph Dokcer
    subgraph fastapi-sqlite1
        fastapi1[FastAPI]
        sqlite1[SQlite]
    end
    subgraph fastapi-sqlite2
        fastapi2[FastAPI]
        sqlite2[SQlite]
    end
    subgraph Volumes
        sqlite-data
    end
    fastapi1-.-sqlite1
    fastapi2-.-sqlite2
    sqlite1<-.->sqlite-data
    sqlite2<-.->sqlite-data
end
```

### Docker Build

```bash
$ docker build -t fastapi-sqlite-app .
```

### Docker Volume

```bash
$ docker volume create sqlite-data
```

### Docker Run 
```bash
$ docker run -d --name fastapi-sqlite1 -v sqlite-data:/data -p 8000:8000 fastapi-sqlite-app
$ docker run -d --name fastapi-sqlite2 -v sqlite-data:/data -p 8001:8000 fastapi-sqlite-app
```

### Docker Compose Build

```bash
$ docker compose build
```

### Docker Compose Run

```bash
$ docker compose up -d
```