# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification176
from . import TerminalManagementDataSet34

class ManagementPlan13(base_types._BaseFieldType):

	__slots__ = ["_DataSet", "_POIId", "_TermnlMgrId"]
	@property
	def DataSet(self):
		return self._DataSet

	@DataSet.setter
	def DataSet(self, value):
		self._DataSet = value if value is not None else base_types.UninitialisedField(self, 'DataSet', TerminalManagementDataSet34, False)

	@DataSet.deleter
	def DataSet(self):
		del self._DataSet
		self._DataSet = base_types.UninitialisedField(self, 'DataSet', TerminalManagementDataSet34, False)

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if value is not None else base_types.UninitialisedField(self, 'POIId', GenericIdentification176, False)

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = base_types.UninitialisedField(self, 'POIId', GenericIdentification176, False)

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
		base_types.FieldEntry(name='DataSet', type=TerminalManagementDataSet34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=GenericIdentification176, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TermnlMgrId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
	))