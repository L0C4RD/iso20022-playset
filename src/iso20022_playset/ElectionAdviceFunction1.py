from . import base_types
from .ElectionType1Code import ElectionType1Code
from .DocumentIdentification8 import DocumentIdentification8

class ElectionAdviceFunction1(base_types._BaseFieldType):

	__slots__ = ["_ElctnTp", "_AgtCAElctnAmdmntReqId", "_AgtCAElctnStsAdvcId", "_PrvsAgtCAElctnAdvcId"]
	@property
	def ElctnTp(self):
		return self._ElctnTp

	@ElctnTp.setter
	def ElctnTp(self, value):
		self._ElctnTp = value if type(value) != auto else self.make_default("ElctnTp")

	@ElctnTp.deleter
	def ElctnTp(self):
		del self._ElctnTp
		self._ElctnTp = None

	@property
	def AgtCAElctnAmdmntReqId(self):
		return self._AgtCAElctnAmdmntReqId

	@AgtCAElctnAmdmntReqId.setter
	def AgtCAElctnAmdmntReqId(self, value):
		self._AgtCAElctnAmdmntReqId = value if type(value) != auto else self.make_default("AgtCAElctnAmdmntReqId")

	@AgtCAElctnAmdmntReqId.deleter
	def AgtCAElctnAmdmntReqId(self):
		del self._AgtCAElctnAmdmntReqId
		self._AgtCAElctnAmdmntReqId = None

	@property
	def AgtCAElctnStsAdvcId(self):
		return self._AgtCAElctnStsAdvcId

	@AgtCAElctnStsAdvcId.setter
	def AgtCAElctnStsAdvcId(self, value):
		self._AgtCAElctnStsAdvcId = value if type(value) != auto else self.make_default("AgtCAElctnStsAdvcId")

	@AgtCAElctnStsAdvcId.deleter
	def AgtCAElctnStsAdvcId(self):
		del self._AgtCAElctnStsAdvcId
		self._AgtCAElctnStsAdvcId = None

	@property
	def PrvsAgtCAElctnAdvcId(self):
		return self._PrvsAgtCAElctnAdvcId

	@PrvsAgtCAElctnAdvcId.setter
	def PrvsAgtCAElctnAdvcId(self, value):
		self._PrvsAgtCAElctnAdvcId = value if type(value) != auto else self.make_default("PrvsAgtCAElctnAdvcId")

	@PrvsAgtCAElctnAdvcId.deleter
	def PrvsAgtCAElctnAdvcId(self):
		del self._PrvsAgtCAElctnAdvcId
		self._PrvsAgtCAElctnAdvcId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElctnTp', type=ElectionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAElctnAmdmntReqId', type=DocumentIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCAElctnStsAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsAgtCAElctnAdvcId', type=DocumentIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

