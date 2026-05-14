# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorConfigurationDataSet7 import AcceptorConfigurationDataSet7
from ._GenericIdentification176 import GenericIdentification176
from ._Max35Text import Max35Text

class AcceptorConfiguration15(base_types._BaseFieldType):

	__slots__ = ["_DataSet", "_POIGrpId", "_TermnlMgrId"]
	@property
	def DataSet(self):
		return self._DataSet

	@DataSet.setter
	def DataSet(self, value):
		self._DataSet = value if type(value) != base_types.auto else self.make_default("DataSet")

	@DataSet.deleter
	def DataSet(self):
		del self._DataSet
		self._DataSet = None

	@property
	def POIGrpId(self):
		return self._POIGrpId

	@POIGrpId.setter
	def POIGrpId(self, value):
		self._POIGrpId = value if type(value) != base_types.auto else self.make_default("POIGrpId")

	@POIGrpId.deleter
	def POIGrpId(self):
		del self._POIGrpId
		self._POIGrpId = None

	@property
	def TermnlMgrId(self):
		return self._TermnlMgrId

	@TermnlMgrId.setter
	def TermnlMgrId(self, value):
		self._TermnlMgrId = value if type(value) != base_types.auto else self.make_default("TermnlMgrId")

	@TermnlMgrId.deleter
	def TermnlMgrId(self):
		del self._TermnlMgrId
		self._TermnlMgrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSet', type=AcceptorConfigurationDataSet7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='POIGrpId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TermnlMgrId', type=GenericIdentification176, min=1, max=1, mutex_group=None, array=False),
	))