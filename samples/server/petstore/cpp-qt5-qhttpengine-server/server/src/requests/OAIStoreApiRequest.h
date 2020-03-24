/**
 * OpenAPI Petstore
 * This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIStoreApiRequest_H
#define OAI_OAIStoreApiRequest_H

#include <QObject>
#include <QStringList>
#include <QMultiMap>
#include <QNetworkReply>
#include <QSharedPointer>

#include <qhttpengine/socket.h>
#include "OAIOrder.h"
#include <QMap>
#include <QString>
#include "OAIStoreApiHandler.h"

namespace OpenAPI {

class OAIStoreApiRequest : public QObject
{
    Q_OBJECT

public:
    OAIStoreApiRequest(QHttpEngine::Socket *s, QSharedPointer<OAIStoreApiHandler> handler);
    virtual ~OAIStoreApiRequest();

    void deleteOrderRequest(const QString& order_id);
    void getInventoryRequest();
    void getOrderByIdRequest(const QString& order_id);
    void placeOrderRequest();
    

    void deleteOrderResponse();
    void getInventoryResponse(const QMap<QString, qint32>& res);
    void getOrderByIdResponse(const OAIOrder& res);
    void placeOrderResponse(const OAIOrder& res);
    

    void deleteOrderError(QNetworkReply::NetworkError error_type, QString& error_str);
    void getInventoryError(const QMap<QString, qint32>& res, QNetworkReply::NetworkError error_type, QString& error_str);
    void getOrderByIdError(const OAIOrder& res, QNetworkReply::NetworkError error_type, QString& error_str);
    void placeOrderError(const OAIOrder& res, QNetworkReply::NetworkError error_type, QString& error_str);
    

    void sendCustomResponse(QByteArray & res, QNetworkReply::NetworkError error_type);

    void sendCustomResponse(QIODevice *res, QNetworkReply::NetworkError error_type);

    QMap<QString, QString> getRequestHeaders() const;

    QHttpEngine::Socket* getRawSocket();

    void setResponseHeaders(const QMultiMap<QString,QString>& headers);

signals:
    void deleteOrder(QString order_id);
    void getInventory();
    void getOrderById(qint64 order_id);
    void placeOrder(OAIOrder body);
    

private:
    QMap<QString, QString> requestHeaders;
    QMap<QString, QString> responseHeaders;
    QHttpEngine::Socket  *socket;
    QSharedPointer<OAIStoreApiHandler> handler;

    inline void writeResponseHeaders(){
        QHttpEngine::Socket::HeaderMap resHeaders;
        for(auto itr = responseHeaders.begin(); itr != responseHeaders.end(); ++itr) {
            resHeaders.insert(itr.key().toUtf8(), itr.value().toUtf8());
        }
        socket->setHeaders(resHeaders);
        socket->writeHeaders();
    }
};

}

#endif // OAI_OAIStoreApiRequest_H
