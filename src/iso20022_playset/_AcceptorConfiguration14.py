# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorConfigurationDataSet6
from . import GenericIdentification176
from . import Max35Text

class AcceptorConfiguration14(base_types._BaseFieldType):

	__slots__ = ["_DataSet", "_POIGrpId", "_TermnlMgrId"]
	@property
	def DataSet(self):
		return self._DataSet

	@DataSet.setter
	def DataSet(self, value):
		self._DataSet = value if value is not None else base_types.UninitialisedField(self, 'DataSet', AcceptorConfigurationDataSet6, True)

	@DataSet.deleter
	def DataSet(self):
		del self._DataSet
		self._DataSet = base_types.UninitialisedField(self, 'DataSet', AcceptorConfigurationDataSet6, True)

	@property
	def POIGrpId(self):
		return self._POIGrpId

	@POIGrpId.setter
	def POIGrpId(self, value):
		self._POIGrpId = value if value is not None else base_types.UninitialisedField(self, 'POIGrpId', Max35Text, True)

	@POIGrpId.deleter
	def POIGrpId(self):
		del self._POIGrpId
		self._POIGrpId = base_types.UninitialisedField(self, 'POIGrpId', Max35Text, True)

	@property
	def TermnlMgrId(self):
		return self._TermnlMgrId

	@TermnlMgrId.setter
	def TermnlMgrId(self, value):
		self._TermnlMgrId = value if value is not None else base_types.UninitialisedField(self, 'TermnlMgrId', GenericIdentification176, False)

	@TermnlMgrId.deleter
	def TermnlMgrId(self):
		del self._TermnlMgrId
		self._TermnlMgrId = base_types.UninitialisedField(self, 'TermnlMgrId', GenericIdentification176, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSet', type=AcceptorConfigurationDataSet6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIGrpId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TermnlMgrId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
	))