# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CertificateReference2
from . import Exact1NumericText
from . import Exact5NumericText
from . import ISODate

class TransactionCertificate5(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_LclInstrm", "_RfrdDoc", "_TxDt", "_TxTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def LclInstrm(self):
		return self._LclInstrm

	@LclInstrm.setter
	def LclInstrm(self, value):
		self._LclInstrm = value if value is not None else base_types.UninitialisedField(self, 'LclInstrm', Exact5NumericText, False)

	@LclInstrm.deleter
	def LclInstrm(self):
		del self._LclInstrm
		self._LclInstrm = base_types.UninitialisedField(self, 'LclInstrm', Exact5NumericText, False)

	@property
	def RfrdDoc(self):
		return self._RfrdDoc

	@RfrdDoc.setter
	def RfrdDoc(self, value):
		self._RfrdDoc = value if value is not None else base_types.UninitialisedField(self, 'RfrdDoc', CertificateReference2, False)

	@RfrdDoc.deleter
	def RfrdDoc(self):
		del self._RfrdDoc
		self._RfrdDoc = base_types.UninitialisedField(self, 'RfrdDoc', CertificateReference2, False)

	@property
	def TxDt(self):
		return self._TxDt

	@TxDt.setter
	def TxDt(self, value):
		self._TxDt = value if value is not None else base_types.UninitialisedField(self, 'TxDt', ISODate, False)

	@TxDt.deleter
	def TxDt(self):
		del self._TxDt
		self._TxDt = base_types.UninitialisedField(self, 'TxDt', ISODate, False)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', Exact1NumericText, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', Exact1NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclInstrm', type=Exact5NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrdDoc', type=CertificateReference2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
	))