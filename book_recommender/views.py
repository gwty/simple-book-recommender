from rest_framework import viewsets
from django.contrib.auth.models import User
from book_recommender.models import Book, Author, CustomUser, FavoriteBooks, BookShelf
from book_recommender.serializers import (
    BookSerializer,
    AuthorSerializer,
    BookShelfSerializer,
    FavoriteBooksSerializer,
    ProfileSerializer,
    RegisterSerializer,
    MyTokenObtainPairSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
from rest_framework import status
from rest_framework import filters

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def index(request):
    if request.method == 'GET':
        return Response({'message': 'Hello, world!'}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        # your logic here
        return Response(data, status=status.HTTP_201_CREATED)

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def get(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    

#api/profile  and api/profile/update
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author_name']
    
    @permission_classes([IsAuthenticated])
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    """
    Retrieve, update or delete a book instance.
    """
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
    @permission_classes([AllowAny])
    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    

    @permission_classes([IsAuthenticated])
    def post(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @permission_classes([IsAuthenticated])
    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = BookSerializer
    @permission_classes([AllowAny])
    def get(self, request, format=None):
        snippets = Author.objects.all()
        serializer = BookSerializer(snippets, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AuthorDetail(APIView):
    """
    Retrieve, update or delete a author instance.
    """
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404
    @permission_classes([AllowAny])
    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @permission_classes([IsAuthenticated])
    def put(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk, format=None):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BookShelfViewSet(viewsets.ModelViewSet):
    queryset = BookShelf.objects.all()
    serializer_class = BookShelfSerializer
    @permission_classes([AllowAny])
    def get(self, request, format=None):
        snippets = Book.objects.all()
        serializer = BookSerializer(snippets, many=True)
        return Response(serializer.data)
    
    @permission_classes([IsAuthenticated])
    def post(self, request, format=None):
        serializer = BookShelfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookShelfDetail(APIView):
    """
    Retrieve, update or delete a bookshelf instance.
    """
    def get_object(self, pk):
        try:
            return BookShelf.objects.get(pk=pk)
        except BookShelf.DoesNotExist:
            raise Http404
    @permission_classes([AllowAny])
    def get(self, request, pk, format=None):
        bookshelf = self.get_object(pk)
        serializer = BookShelfSerializer(bookshelf)
        return Response(serializer.data)
    

    @permission_classes([IsAuthenticated])
    def post(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookShelfSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @permission_classes([IsAuthenticated])
    def put(self, request, pk, format=None):
        bookshelf = self.get_object(pk)
        serializer = BookShelfSerializer(bookshelf, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk, format=None):
        bookshelf = self.get_object(pk)
        bookshelf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FavoriteBooksViewSet(viewsets.ModelViewSet):
    queryset = FavoriteBooks.objects.all()
    serializer_class = FavoriteBooksSerializer
    @permission_classes([AllowAny])
    def get(self, request, format=None):
        favoritebooks = FavoriteBooks.objects.all()
        serializer = FavoriteBooksSerializer(favoritebooks, many=True)
        return Response(serializer.data)
    
    @permission_classes([IsAuthenticated])
    def post(self, request, format=None):
        serializer = FavoriteBooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FavoriteBooksDetail(APIView):
    """
    Retrieve, update or delete a favorite books instance.
    """
    def get_object(self, pk):
        try:
            return FavoriteBooks.objects.get(pk=pk)
        except FavoriteBooks.DoesNotExist:
            raise Http404
    @permission_classes([AllowAny])
    def get(self, request, pk, format=None):
        favoritebooks = self.get_object(pk)
        serializer = BookShelfSerializer(favoritebooks)
        return Response(serializer.data)
    

    @permission_classes([IsAuthenticated])
    def post(self, request, pk, format=None):
        favoritebooks = self.get_object(pk)
        serializer = BookShelfSerializer(favoritebooks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @permission_classes([IsAuthenticated])
    def put(self, request, pk, format=None):
        favoritebooks = self.get_object(pk)
        serializer = FavoriteBooksSerializer(favoritebooks, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, request, pk, format=None):
        favoritebooks = self.get_object(pk)
        favoritebooks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SuggestedBooks(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user_id = -1
        # some shelves are too common, so we can blacklist them
        blacklist_shelves = ['to-read','currently-reading','favorites','owned']
        if 'user_id' in request.data:
            user_id = request.data['user_id']

            # get favorite books
            favoritebooks = FavoriteBooks.objects.filter(user_id=user_id)
            favoritebooks_serializer = FavoriteBooksSerializer(favoritebooks, many=True)
            favorite_book_ids = []
            for books in favoritebooks_serializer.data:
                favorite_book_ids.append(books['book_id']) 
            
            # get popular shelves of favorite books
            shelves = BookShelf.objects.filter(book_id__in=favorite_book_ids)
            shelves_serializer = BookShelfSerializer(shelves, many=True)
            shelf_counts = {}
            for shelf in shelves_serializer.data:
                if shelf['shelf_name'] in blacklist_shelves:
                    continue
                if shelf['shelf_name'] not in shelf_counts:
                    shelf_counts[shelf['shelf_name']] = 0
                shelf_counts[shelf['shelf_name']] += shelf['shelf_count']
                
            # get top 10 shelves
            suggested_shelves = sorted(shelf_counts.items(), key = lambda x:x[1], reverse=True)[:10]
            suggested_shelves_names = list(x[0] for x in suggested_shelves)

            # get top 1000 books in the shelves
            suggested_books_1 = BookShelf.objects.filter(shelf_name__in=suggested_shelves_names).order_by('-shelf_count')[:1000]
            suggested_books_1_serializer = BookShelfSerializer(suggested_books_1, many=True)

            suggested_books_1_ids = []
            for books in suggested_books_1_serializer.data:
                suggested_books_1_ids.append(books['book_id'])  

            # get top 5 books in the shelves ordered by average rating (highest first)
            suggested_books_2 = Book.objects.filter(book_id__in=suggested_books_1_ids).order_by('-average_rating')[:5]
            suggested_books_2_serializer = BookSerializer(suggested_books_2, many=True)
            return Response(suggested_books_2_serializer.data)
        

        return Response(status=status.HTTP_204_NO_CONTENT)


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)