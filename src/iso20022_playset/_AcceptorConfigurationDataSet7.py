# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorConfigurationContent15
from . import DataSetIdentification11
from . import GenericIdentification176
from . import Max9NumericText
from . import PartyType15Code
from . import TrueFalseIndicator

class AcceptorConfigurationDataSet7(base_types._BaseFieldType):

	__slots__ = ["_CfgtnScp", "_Cntt", "_Id", "_LastSeq", "_POIId", "_SeqCntr"]
	@property
	def CfgtnScp(self):
		return self._CfgtnScp

	@CfgtnScp.setter
	def CfgtnScp(self, value):
		self._CfgtnScp = value if value is not None else base_types.UninitialisedField(self, 'CfgtnScp', PartyType15Code, False)

	@CfgtnScp.deleter
	def CfgtnScp(self):
		del self._CfgtnScp
		self._CfgtnScp = base_types.UninitialisedField(self, 'CfgtnScp', PartyType15Code, False)

	@property
	def Cntt(self):
		return self._Cntt

	@Cntt.setter
	def Cntt(self, value):
		self._Cntt = value if value is not None else base_types.UninitialisedField(self, 'Cntt', AcceptorConfigurationContent15, False)

	@Cntt.deleter
	def Cntt(self):
		del self._Cntt
		self._Cntt = base_types.UninitialisedField(self, 'Cntt', AcceptorConfigurationContent15, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', DataSetIdentification11, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', DataSetIdentification11, False)

	@property
	def LastSeq(self):
		return self._LastSeq

	@LastSeq.setter
	def LastSeq(self, value):
		self._LastSeq = value if value is not None else base_types.UninitialisedField(self, 'LastSeq', TrueFalseIndicator, False)

	@LastSeq.deleter
	def LastSeq(self):
		del self._LastSeq
		self._LastSeq = base_types.UninitialisedField(self, 'LastSeq', TrueFalseIndicator, False)

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if value is not None else base_types.UninitialisedField(self, 'POIId', GenericIdentification176, True)

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = base_types.UninitialisedField(self, 'POIId', GenericIdentification176, True)

	@property
	def SeqCntr(self):
		return self._SeqCntr

	@SeqCntr.setter
	def SeqCntr(self, value):
		self._SeqCntr = value if value is not None else base_types.UninitialisedField(self, 'SeqCntr', Max9NumericText, False)

	@SeqCntr.deleter
	def SeqCntr(self):
		del self._SeqCntr
		self._SeqCntr = base_types.UninitialisedField(self, 'SeqCntr', Max9NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CfgtnScp', type=PartyType15Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntt', type=AcceptorConfigurationContent15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DataSetIdentification11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastSeq', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=GenericIdentification176, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SeqCntr', type=Max9NumericText, min=0, max=1, mutex_group=None, array=False),
	))