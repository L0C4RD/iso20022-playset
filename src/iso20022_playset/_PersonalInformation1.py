from . import base_types
from .Max35Text import Max35Text

class PersonalInformation1(base_types._BaseFieldType):

	__slots__ = ["_MdnNmOfMthr", "_NmOfPrtnr", "_NmOfFthr"]
	@property
	def MdnNmOfMthr(self):
		return self._MdnNmOfMthr

	@MdnNmOfMthr.setter
	def MdnNmOfMthr(self, value):
		self._MdnNmOfMthr = value if type(value) != base_types.auto else self.make_default("MdnNmOfMthr")

	@MdnNmOfMthr.deleter
	def MdnNmOfMthr(self):
		del self._MdnNmOfMthr
		self._MdnNmOfMthr = None

	@property
	def NmOfPrtnr(self):
		return self._NmOfPrtnr

	@NmOfPrtnr.setter
	def NmOfPrtnr(self, value):
		self._NmOfPrtnr = value if type(value) != base_types.auto else self.make_default("NmOfPrtnr")

	@NmOfPrtnr.deleter
	def NmOfPrtnr(self):
		del self._NmOfPrtnr
		self._NmOfPrtnr = None

	@property
	def NmOfFthr(self):
		return self._NmOfFthr

	@NmOfFthr.setter
	def NmOfFthr(self, value):
		self._NmOfFthr = value if type(value) != base_types.auto else self.make_default("NmOfFthr")

	@NmOfFthr.deleter
	def NmOfFthr(self):
		del self._NmOfFthr
		self._NmOfFthr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MdnNmOfMthr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmOfPrtnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmOfFthr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

