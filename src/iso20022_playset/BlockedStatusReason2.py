from . import base_types
import Max350Text
import BlockedReason2Choice
import TransactionType5Choice
import YesNoIndicator

class BlockedStatusReason2(base_types._BaseFieldType):

	__slots__ = ["_Blckd", "_Rsn", "_AddtlInf", "_TxTp"]
	@property
	def Blckd(self):
		return self._Blckd

	@Blckd.setter
	def Blckd(self, value):
		self._Blckd = value if type(value) != auto else self.make_default("Blckd")

	@Blckd.deleter
	def Blckd(self):
		del self._Blckd
		self._Blckd = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Blckd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=BlockedReason2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=TransactionType5Choice, min=1, max=1, mutex_group=None, array=False),
	))

