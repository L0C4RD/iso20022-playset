import base_types
import Exact1NumericText
import Exact5NumericText
import ISODate
import ActiveCurrencyAndAmount
import CertificateReference2

class TransactionCertificate5(base_types._BaseFieldType):

	__slots__ = ["_TxTp", "_RfrdDoc", "_LclInstrm", "_Amt", "_TxDt"]
	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	@property
	def RfrdDoc(self):
		return self._RfrdDoc

	@RfrdDoc.setter
	def RfrdDoc(self, value):
		self._RfrdDoc = value if type(value) != auto else self.make_default("RfrdDoc")

	@RfrdDoc.deleter
	def RfrdDoc(self):
		del self._RfrdDoc
		self._RfrdDoc = None

	@property
	def LclInstrm(self):
		return self._LclInstrm

	@LclInstrm.setter
	def LclInstrm(self, value):
		self._LclInstrm = value if type(value) != auto else self.make_default("LclInstrm")

	@LclInstrm.deleter
	def LclInstrm(self):
		del self._LclInstrm
		self._LclInstrm = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def TxDt(self):
		return self._TxDt

	@TxDt.setter
	def TxDt(self, value):
		self._TxDt = value if type(value) != auto else self.make_default("TxDt")

	@TxDt.deleter
	def TxDt(self):
		del self._TxDt
		self._TxDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxTp', type=Exact1NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrdDoc', type=CertificateReference2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclInstrm', type=Exact5NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

