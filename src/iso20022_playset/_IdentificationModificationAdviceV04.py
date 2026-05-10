from . import base_types
from ._IdentificationAssignment4 import IdentificationAssignment4
from ._IdentificationModification5 import IdentificationModification5
from ._OriginalTransactionReference43 import OriginalTransactionReference43
from ._SupplementaryData1 import SupplementaryData1

class IdentificationModificationAdviceV04(base_types._BaseFieldType):

	__slots__ = ["_Assgnmt", "_Mod", "_OrgnlTxRef", "_SplmtryData"]
	@property
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if type(value) != base_types.auto else self.make_default("Assgnmt")

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = None

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != base_types.auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if type(value) != base_types.auto else self.make_default("OrgnlTxRef")

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgnmt', type=IdentificationAssignment4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mod', type=IdentificationModification5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

