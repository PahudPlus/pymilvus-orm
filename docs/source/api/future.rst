======
Future
======


SearchResultFuture
------------------

Constructor
~~~~~~~~~~~

+----------------------------------------------------------------------+------------------------------------------------------------------------+
| Constructor                                                          | Description                                                            |
+======================================================================+========================================================================+
| `SearchResultFuture() <#pymilvus_orm.SearchResultFuture>`_           | Search result future.                                                  |
+----------------------------------------------------------------------+------------------------------------------------------------------------+

Attributes
~~~~~~~~~~

+----------------------------------------------------------------------+------------------------------------------------------------------------+
| API                                                                  | Description                                                            |
+======================================================================+========================================================================+
| `result() <#pymilvus_orm.SearchResultFuture.result>`_                | Return the search result.                                              |
+----------------------------------------------------------------------+------------------------------------------------------------------------+
| `cancel() <#pymilvus_orm.SearchResultFuture.cancel>`_                | Cancel the search request.                                             |
+----------------------------------------------------------------------+------------------------------------------------------------------------+
| `done() <#pymilvus_orm.SearchResultFuture.done>`_                    | Wait for search request done.                                          |
+----------------------------------------------------------------------+------------------------------------------------------------------------+


APIs References
~~~~~~~~~~~~~~~


.. autoclass:: pymilvus_orm.SearchResultFuture
   :member-order: bysource
   :members: result, cancel, done


InsertFuture
------------

Constructor
~~~~~~~~~~~

+----------------------------------------------------------------------+------------------------------------------------------------------------+
| Constructor                                                          | Description                                                            |
+======================================================================+========================================================================+
| `InsertFuture() <#pymilvus_orm.InsertFuture>`_                       | Insert future.                                                         |
+----------------------------------------------------------------------+------------------------------------------------------------------------+

Attributes
~~~~~~~~~~

+----------------------------------------------------------------------+------------------------------------------------------------------------+
| API                                                                  | Description                                                            |
+======================================================================+========================================================================+
| `result() <#pymilvus_orm.InsertFuture.result>`_                      | Return the insert result.                                              |
+----------------------------------------------------------------------+------------------------------------------------------------------------+
| `cancel() <#pymilvus_orm.InsertFuture.cancel>`_                      | Cancel the insert request.                                             |
+----------------------------------------------------------------------+------------------------------------------------------------------------+
| `done() <#pymilvus_orm.InsertFuture.done>`_                          | Wait for insert request done.                                          |
+----------------------------------------------------------------------+------------------------------------------------------------------------+


APIs References
~~~~~~~~~~~~~~~


.. autoclass:: pymilvus_orm.InsertFuture
   :member-order: bysource
   :members: result, cancel, done
