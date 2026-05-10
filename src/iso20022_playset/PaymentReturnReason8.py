import base_types
import Max105Text
import BankTransactionCodeStructure4
import PartyIdentification272
import ReturnReason5Choice

class PaymentReturnReason8(base_types._BaseFieldType):

	__slots__ = ["_Orgtr", "_OrgnlBkTxCd", "_Rsn", "_AddtlInf"]
	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if type(value) != auto else self.make_default("Orgtr")

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = None

	@property
	def OrgnlBkTxCd(self):
		return self._OrgnlBkTxCd

	@OrgnlBkTxCd.setter
	def OrgnlBkTxCd(self, value):
		self._OrgnlBkTxCd = value if type(value) != auto else self.make_default("OrgnlBkTxCd")

	@OrgnlBkTxCd.deleter
	def OrgnlBkTxCd(self):
		del self._OrgnlBkTxCd
		self._OrgnlBkTxCd = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Orgtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBkTxCd', type=BankTransactionCodeStructure4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=ReturnReason5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max105Text, min=0, max=None, mutex_group=None, array=True),
	))

