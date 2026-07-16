# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageIdentification1
from . import SimpleIdentificationInformation

class RoleAndBaselineAcceptanceV01(base_types._BaseFieldType):

	__slots__ = ["_AccptncId", "_RltdMsgRef", "_TxId"]
	@property
	def AccptncId(self):
		return self._AccptncId

	@AccptncId.setter
	def AccptncId(self, value):
		self._AccptncId = value if value is not None else base_types.UninitialisedField(self, 'AccptncId', MessageIdentification1, False)

	@AccptncId.deleter
	def AccptncId(self):
		del self._AccptncId
		self._AccptncId = base_types.UninitialisedField(self, 'AccptncId', MessageIdentification1, False)

	@property
	def RltdMsgRef(self):
		return self._RltdMsgRef

	@RltdMsgRef.setter
	def RltdMsgRef(self, value):
		self._RltdMsgRef = value if value is not None else base_types.UninitialisedField(self, 'RltdMsgRef', MessageIdentification1, False)

	@RltdMsgRef.deleter
	def RltdMsgRef(self):
		del self._RltdMsgRef
		self._RltdMsgRef = base_types.UninitialisedField(self, 'RltdMsgRef', MessageIdentification1, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', SimpleIdentificationInformation, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', SimpleIdentificationInformation, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptncId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdMsgRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
	))