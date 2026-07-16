# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import RemittanceLocationData2
from . import TransactionReferences8

class RemittanceLocation10(base_types._BaseFieldType):

	__slots__ = ["_Refs", "_RmtId", "_RmtLctnDtls"]
	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if value is not None else base_types.UninitialisedField(self, 'Refs', TransactionReferences8, False)

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = base_types.UninitialisedField(self, 'Refs', TransactionReferences8, False)

	@property
	def RmtId(self):
		return self._RmtId

	@RmtId.setter
	def RmtId(self, value):
		self._RmtId = value if value is not None else base_types.UninitialisedField(self, 'RmtId', Max35Text, False)

	@RmtId.deleter
	def RmtId(self):
		del self._RmtId
		self._RmtId = base_types.UninitialisedField(self, 'RmtId', Max35Text, False)

	@property
	def RmtLctnDtls(self):
		return self._RmtLctnDtls

	@RmtLctnDtls.setter
	def RmtLctnDtls(self, value):
		self._RmtLctnDtls = value if value is not None else base_types.UninitialisedField(self, 'RmtLctnDtls', RemittanceLocationData2, True)

	@RmtLctnDtls.deleter
	def RmtLctnDtls(self):
		del self._RmtLctnDtls
		self._RmtLctnDtls = base_types.UninitialisedField(self, 'RmtLctnDtls', RemittanceLocationData2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Refs', type=TransactionReferences8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtLctnDtls', type=RemittanceLocationData2, min=1, max=None, mutex_group=None, array=True),
	))