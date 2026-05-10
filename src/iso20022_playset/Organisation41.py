from . import base_types
from .CommunicationAddress9 import CommunicationAddress9
from .Max140Text import Max140Text
from .Max70Text import Max70Text
from .LocationCategory4Code import LocationCategory4Code
from .GenericIdentification32 import GenericIdentification32

class Organisation41(base_types._BaseFieldType):

	__slots__ = ["_LctnCtgy", "_LctnAndCtct", "_SchmeData", "_CmonNm", "_Id"]
	@property
	def LctnCtgy(self):
		return self._LctnCtgy

	@LctnCtgy.setter
	def LctnCtgy(self, value):
		self._LctnCtgy = value if type(value) != auto else self.make_default("LctnCtgy")

	@LctnCtgy.deleter
	def LctnCtgy(self):
		del self._LctnCtgy
		self._LctnCtgy = None

	@property
	def LctnAndCtct(self):
		return self._LctnAndCtct

	@LctnAndCtct.setter
	def LctnAndCtct(self, value):
		self._LctnAndCtct = value if type(value) != auto else self.make_default("LctnAndCtct")

	@LctnAndCtct.deleter
	def LctnAndCtct(self):
		del self._LctnAndCtct
		self._LctnAndCtct = None

	@property
	def SchmeData(self):
		return self._SchmeData

	@SchmeData.setter
	def SchmeData(self, value):
		self._SchmeData = value if type(value) != auto else self.make_default("SchmeData")

	@SchmeData.deleter
	def SchmeData(self):
		del self._SchmeData
		self._SchmeData = None

	@property
	def CmonNm(self):
		return self._CmonNm

	@CmonNm.setter
	def CmonNm(self, value):
		self._CmonNm = value if type(value) != auto else self.make_default("CmonNm")

	@CmonNm.deleter
	def CmonNm(self):
		del self._CmonNm
		self._CmonNm = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='LctnCtgy', type=LocationCategory4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LctnAndCtct', type=CommunicationAddress9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchmeData', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification32, min=0, max=1, mutex_group=None, array=False),
	))

