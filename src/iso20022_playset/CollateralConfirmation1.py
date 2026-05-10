from . import base_types
import CollateralSubstitutionConfirmation1Code
import Max140Text
import Max35Text

class CollateralConfirmation1(base_types._BaseFieldType):

	__slots__ = ["_ConfTp", "_CollSbstitnReqId", "_Cmnt", "_CollSbstitnRspnId"]
	@property
	def ConfTp(self):
		return self._ConfTp

	@ConfTp.setter
	def ConfTp(self, value):
		self._ConfTp = value if type(value) != auto else self.make_default("ConfTp")

	@ConfTp.deleter
	def ConfTp(self):
		del self._ConfTp
		self._ConfTp = None

	@property
	def CollSbstitnReqId(self):
		return self._CollSbstitnReqId

	@CollSbstitnReqId.setter
	def CollSbstitnReqId(self, value):
		self._CollSbstitnReqId = value if type(value) != auto else self.make_default("CollSbstitnReqId")

	@CollSbstitnReqId.deleter
	def CollSbstitnReqId(self):
		del self._CollSbstitnReqId
		self._CollSbstitnReqId = None

	@property
	def Cmnt(self):
		return self._Cmnt

	@Cmnt.setter
	def Cmnt(self, value):
		self._Cmnt = value if type(value) != auto else self.make_default("Cmnt")

	@Cmnt.deleter
	def Cmnt(self):
		del self._Cmnt
		self._Cmnt = None

	@property
	def CollSbstitnRspnId(self):
		return self._CollSbstitnRspnId

	@CollSbstitnRspnId.setter
	def CollSbstitnRspnId(self, value):
		self._CollSbstitnRspnId = value if type(value) != auto else self.make_default("CollSbstitnRspnId")

	@CollSbstitnRspnId.deleter
	def CollSbstitnRspnId(self):
		del self._CollSbstitnRspnId
		self._CollSbstitnRspnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfTp', type=CollateralSubstitutionConfirmation1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmnt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnRspnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

