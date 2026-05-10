import base_types
import Max35Text
import AcceptorConfigurationDataSet6
import GenericIdentification176

class AcceptorConfiguration14(base_types._BaseFieldType):

	__slots__ = ["_POIGrpId", "_DataSet", "_TermnlMgrId"]
	@property
	def POIGrpId(self):
		return self._POIGrpId

	@POIGrpId.setter
	def POIGrpId(self, value):
		self._POIGrpId = value if type(value) != auto else self.make_default("POIGrpId")

	@POIGrpId.deleter
	def POIGrpId(self):
		del self._POIGrpId
		self._POIGrpId = None

	@property
	def DataSet(self):
		return self._DataSet

	@DataSet.setter
	def DataSet(self, value):
		self._DataSet = value if type(value) != auto else self.make_default("DataSet")

	@DataSet.deleter
	def DataSet(self):
		del self._DataSet
		self._DataSet = None

	@property
	def TermnlMgrId(self):
		return self._TermnlMgrId

	@TermnlMgrId.setter
	def TermnlMgrId(self, value):
		self._TermnlMgrId = value if type(value) != auto else self.make_default("TermnlMgrId")

	@TermnlMgrId.deleter
	def TermnlMgrId(self):
		del self._TermnlMgrId
		self._TermnlMgrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='POIGrpId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DataSet', type=AcceptorConfigurationDataSet6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TermnlMgrId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
	))

