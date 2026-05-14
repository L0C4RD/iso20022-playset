from . import base_types
from ._ClassificationType4 import ClassificationType4
from ._Document28 import Document28
from ._GenericIdentification175 import GenericIdentification175
from ._PartyIdentification260Choice import PartyIdentification260Choice
from ._SecurityIdentification49 import SecurityIdentification49

class MetadataReport5(base_types._BaseFieldType):

	__slots__ = ["_ColltnBody", "_RgltryData", "_RgltryDataTp", "_RltdNtty", "_RltdPdctIdr", "_SubmitgNtty"]
	@property
	def ColltnBody(self):
		return self._ColltnBody

	@ColltnBody.setter
	def ColltnBody(self, value):
		self._ColltnBody = value if type(value) != base_types.auto else self.make_default("ColltnBody")

	@ColltnBody.deleter
	def ColltnBody(self):
		del self._ColltnBody
		self._ColltnBody = None

	@property
	def RgltryData(self):
		return self._RgltryData

	@RgltryData.setter
	def RgltryData(self, value):
		self._RgltryData = value if type(value) != base_types.auto else self.make_default("RgltryData")

	@RgltryData.deleter
	def RgltryData(self):
		del self._RgltryData
		self._RgltryData = None

	@property
	def RgltryDataTp(self):
		return self._RgltryDataTp

	@RgltryDataTp.setter
	def RgltryDataTp(self, value):
		self._RgltryDataTp = value if type(value) != base_types.auto else self.make_default("RgltryDataTp")

	@RgltryDataTp.deleter
	def RgltryDataTp(self):
		del self._RgltryDataTp
		self._RgltryDataTp = None

	@property
	def RltdNtty(self):
		return self._RltdNtty

	@RltdNtty.setter
	def RltdNtty(self, value):
		self._RltdNtty = value if type(value) != base_types.auto else self.make_default("RltdNtty")

	@RltdNtty.deleter
	def RltdNtty(self):
		del self._RltdNtty
		self._RltdNtty = None

	@property
	def RltdPdctIdr(self):
		return self._RltdPdctIdr

	@RltdPdctIdr.setter
	def RltdPdctIdr(self, value):
		self._RltdPdctIdr = value if type(value) != base_types.auto else self.make_default("RltdPdctIdr")

	@RltdPdctIdr.deleter
	def RltdPdctIdr(self):
		del self._RltdPdctIdr
		self._RltdPdctIdr = None

	@property
	def SubmitgNtty(self):
		return self._SubmitgNtty

	@SubmitgNtty.setter
	def SubmitgNtty(self, value):
		self._SubmitgNtty = value if type(value) != base_types.auto else self.make_default("SubmitgNtty")

	@SubmitgNtty.deleter
	def SubmitgNtty(self):
		del self._SubmitgNtty
		self._SubmitgNtty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ColltnBody', type=GenericIdentification175, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryData', type=Document28, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RgltryDataTp', type=ClassificationType4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdNtty', type=PartyIdentification260Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdPdctIdr', type=SecurityIdentification49, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubmitgNtty', type=PartyIdentification260Choice, min=0, max=1, mutex_group=None, array=False),
	))

