# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IdentificationAssignment4
from . import IdentificationModification5
from . import OriginalTransactionReference43
from . import SupplementaryData1

class IdentificationModificationAdviceV04(base_types._BaseFieldType):

	__slots__ = ["_Assgnmt", "_Mod", "_OrgnlTxRef", "_SplmtryData"]
	@property
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if value is not None else base_types.UninitialisedField(self, 'Assgnmt', IdentificationAssignment4, False)

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = base_types.UninitialisedField(self, 'Assgnmt', IdentificationAssignment4, False)

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if value is not None else base_types.UninitialisedField(self, 'Mod', IdentificationModification5, True)

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = base_types.UninitialisedField(self, 'Mod', IdentificationModification5, True)

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTxRef', OriginalTransactionReference43, False)

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = base_types.UninitialisedField(self, 'OrgnlTxRef', OriginalTransactionReference43, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgnmt', type=IdentificationAssignment4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mod', type=IdentificationModification5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))