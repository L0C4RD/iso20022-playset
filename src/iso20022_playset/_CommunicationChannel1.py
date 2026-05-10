from . import base_types
from ._ExternalChannel1Code import ExternalChannel1Code
from ._Max140Text import Max140Text
from ._PartyType1Choice import PartyType1Choice
from ._PostalAddress6 import PostalAddress6

class CommunicationChannel1(base_types._BaseFieldType):

	__slots__ = ["_DlvrToAdr", "_DlvrToNm", "_DlvrToPtyTp", "_Mtd"]
	@property
	def DlvrToAdr(self):
		return self._DlvrToAdr

	@DlvrToAdr.setter
	def DlvrToAdr(self, value):
		self._DlvrToAdr = value if type(value) != base_types.auto else self.make_default("DlvrToAdr")

	@DlvrToAdr.deleter
	def DlvrToAdr(self):
		del self._DlvrToAdr
		self._DlvrToAdr = None

	@property
	def DlvrToNm(self):
		return self._DlvrToNm

	@DlvrToNm.setter
	def DlvrToNm(self, value):
		self._DlvrToNm = value if type(value) != base_types.auto else self.make_default("DlvrToNm")

	@DlvrToNm.deleter
	def DlvrToNm(self):
		del self._DlvrToNm
		self._DlvrToNm = None

	@property
	def DlvrToPtyTp(self):
		return self._DlvrToPtyTp

	@DlvrToPtyTp.setter
	def DlvrToPtyTp(self, value):
		self._DlvrToPtyTp = value if type(value) != base_types.auto else self.make_default("DlvrToPtyTp")

	@DlvrToPtyTp.deleter
	def DlvrToPtyTp(self):
		del self._DlvrToPtyTp
		self._DlvrToPtyTp = None

	@property
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if type(value) != base_types.auto else self.make_default("Mtd")

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrToAdr', type=PostalAddress6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrToNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrToPtyTp', type=PartyType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtd', type=ExternalChannel1Code, min=1, max=1, mutex_group=None, array=False),
	))

