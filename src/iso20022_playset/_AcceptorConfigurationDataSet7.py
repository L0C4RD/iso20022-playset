# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorConfigurationContent15 import AcceptorConfigurationContent15
from ._DataSetIdentification11 import DataSetIdentification11
from ._GenericIdentification176 import GenericIdentification176
from ._Max9NumericText import Max9NumericText
from ._PartyType15Code import PartyType15Code
from ._TrueFalseIndicator import TrueFalseIndicator

class AcceptorConfigurationDataSet7(base_types._BaseFieldType):

	__slots__ = ["_CfgtnScp", "_Cntt", "_Id", "_LastSeq", "_POIId", "_SeqCntr"]
	@property
	def CfgtnScp(self):
		return self._CfgtnScp

	@CfgtnScp.setter
	def CfgtnScp(self, value):
		self._CfgtnScp = value if type(value) != base_types.auto else self.make_default("CfgtnScp")

	@CfgtnScp.deleter
	def CfgtnScp(self):
		del self._CfgtnScp
		self._CfgtnScp = None

	@property
	def Cntt(self):
		return self._Cntt

	@Cntt.setter
	def Cntt(self, value):
		self._Cntt = value if type(value) != base_types.auto else self.make_default("Cntt")

	@Cntt.deleter
	def Cntt(self):
		del self._Cntt
		self._Cntt = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def LastSeq(self):
		return self._LastSeq

	@LastSeq.setter
	def LastSeq(self, value):
		self._LastSeq = value if type(value) != base_types.auto else self.make_default("LastSeq")

	@LastSeq.deleter
	def LastSeq(self):
		del self._LastSeq
		self._LastSeq = None

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if type(value) != base_types.auto else self.make_default("POIId")

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = None

	@property
	def SeqCntr(self):
		return self._SeqCntr

	@SeqCntr.setter
	def SeqCntr(self, value):
		self._SeqCntr = value if type(value) != base_types.auto else self.make_default("SeqCntr")

	@SeqCntr.deleter
	def SeqCntr(self):
		del self._SeqCntr
		self._SeqCntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CfgtnScp', type=PartyType15Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntt', type=AcceptorConfigurationContent15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DataSetIdentification11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastSeq', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=GenericIdentification176, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SeqCntr', type=Max9NumericText, min=0, max=1, mutex_group=None, array=False),
	))