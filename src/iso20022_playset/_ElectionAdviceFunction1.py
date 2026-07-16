# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification8
from . import ElectionType1Code

class ElectionAdviceFunction1(base_types._BaseFieldType):

	__slots__ = ["_AgtCAElctnAmdmntReqId", "_AgtCAElctnStsAdvcId", "_ElctnTp", "_PrvsAgtCAElctnAdvcId"]
	@property
	def AgtCAElctnAmdmntReqId(self):
		return self._AgtCAElctnAmdmntReqId

	@AgtCAElctnAmdmntReqId.setter
	def AgtCAElctnAmdmntReqId(self, value):
		self._AgtCAElctnAmdmntReqId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAElctnAmdmntReqId', DocumentIdentification8, False)

	@AgtCAElctnAmdmntReqId.deleter
	def AgtCAElctnAmdmntReqId(self):
		del self._AgtCAElctnAmdmntReqId
		self._AgtCAElctnAmdmntReqId = base_types.UninitialisedField(self, 'AgtCAElctnAmdmntReqId', DocumentIdentification8, False)

	@property
	def AgtCAElctnStsAdvcId(self):
		return self._AgtCAElctnStsAdvcId

	@AgtCAElctnStsAdvcId.setter
	def AgtCAElctnStsAdvcId(self, value):
		self._AgtCAElctnStsAdvcId = value if value is not None else base_types.UninitialisedField(self, 'AgtCAElctnStsAdvcId', DocumentIdentification8, False)

	@AgtCAElctnStsAdvcId.deleter
	def AgtCAElctnStsAdvcId(self):
		del self._AgtCAElctnStsAdvcId
		self._AgtCAElctnStsAdvcId = base_types.UninitialisedField(self, 'AgtCAElctnStsAdvcId', DocumentIdentification8, False)

	@property
	def ElctnTp(self):
		return self._ElctnTp

	@ElctnTp.setter
	def ElctnTp(self, value):
		self._ElctnTp = value if value is not None else base_types.UninitialisedField(self, 'ElctnTp', ElectionType1Code, False)

	@ElctnTp.deleter
	def ElctnTp(self):
		del self._ElctnTp
		self._ElctnTp = base_types.UninitialisedField(self, 'ElctnTp', ElectionType1Code, False)

	@property
	def PrvsAgtCAElctnAdvcId(self):
		return self._PrvsAgtCAElctnAdvcId

	@PrvsAgtCAElctnAdvcId.setter
	def PrvsAgtCAElctnAdvcId(self, value):
		self._PrvsAgtCAElctnAdvcId = value if value is not None else base_types.UninitialisedField(self, 'PrvsAgtCAElctnAdvcId', DocumentIdentification8, False)

	@PrvsAgtCAElctnAdvcId.deleter
	def PrvsAgtCAElctnAdvcId(self):
		del self._PrvsAgtCAElctnAdvcId
		self._PrvsAgtCAElctnAdvcId = base_types.UninitialisedField(self, 'PrvsAgtCAElctnAdvcId', DocumentIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCAElctnAmdmntReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAElctnStsAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctnTp', type=ElectionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsAgtCAElctnAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=None, array=False),
	))