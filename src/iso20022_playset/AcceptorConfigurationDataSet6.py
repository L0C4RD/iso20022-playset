import base_types
import TrueFalseIndicator
import PartyType15Code
import Max9NumericText
import GenericIdentification176
import AcceptorConfigurationContent14
import DataSetIdentification11

class AcceptorConfigurationDataSet6(base_types._BaseFieldType):

	__slots__ = ["_LastSeq", "_SeqCntr", "_Id", "_Cntt", "_POIId", "_CfgtnScp"]
	@property
	def LastSeq(self):
		return self._LastSeq

	@LastSeq.setter
	def LastSeq(self, value):
		self._LastSeq = value if type(value) != auto else self.make_default("LastSeq")

	@LastSeq.deleter
	def LastSeq(self):
		del self._LastSeq
		self._LastSeq = None

	@property
	def SeqCntr(self):
		return self._SeqCntr

	@SeqCntr.setter
	def SeqCntr(self, value):
		self._SeqCntr = value if type(value) != auto else self.make_default("SeqCntr")

	@SeqCntr.deleter
	def SeqCntr(self):
		del self._SeqCntr
		self._SeqCntr = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Cntt(self):
		return self._Cntt

	@Cntt.setter
	def Cntt(self, value):
		self._Cntt = value if type(value) != auto else self.make_default("Cntt")

	@Cntt.deleter
	def Cntt(self):
		del self._Cntt
		self._Cntt = None

	@property
	def POIId(self):
		return self._POIId

	@POIId.setter
	def POIId(self, value):
		self._POIId = value if type(value) != auto else self.make_default("POIId")

	@POIId.deleter
	def POIId(self):
		del self._POIId
		self._POIId = None

	@property
	def CfgtnScp(self):
		return self._CfgtnScp

	@CfgtnScp.setter
	def CfgtnScp(self, value):
		self._CfgtnScp = value if type(value) != auto else self.make_default("CfgtnScp")

	@CfgtnScp.deleter
	def CfgtnScp(self):
		del self._CfgtnScp
		self._CfgtnScp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LastSeq', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqCntr', type=Max9NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DataSetIdentification11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntt', type=AcceptorConfigurationContent14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIId', type=GenericIdentification176, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CfgtnScp', type=PartyType15Code, min=0, max=1, mutex_group=None, array=False),
	))

