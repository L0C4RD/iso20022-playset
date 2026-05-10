from . import base_types
from .CountryCode import CountryCode
from .Max10Text import Max10Text
from .Max20000Text import Max20000Text
from .SupervisingAuthorityIdentification1Choice import SupervisingAuthorityIdentification1Choice
from .PostalAddress6 import PostalAddress6
from .Max350Text import Max350Text
from .CommunicationAddress7 import CommunicationAddress7

class PartyDetail1(base_types._BaseFieldType):

	__slots__ = ["_PstlAdr", "_PtyTp", "_FullNm", "_Ctct", "_SprvsgAuthrty", "_Cmnt", "_Ctry"]
	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if type(value) != auto else self.make_default("PstlAdr")

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = None

	@property
	def PtyTp(self):
		return self._PtyTp

	@PtyTp.setter
	def PtyTp(self, value):
		self._PtyTp = value if type(value) != auto else self.make_default("PtyTp")

	@PtyTp.deleter
	def PtyTp(self):
		del self._PtyTp
		self._PtyTp = None

	@property
	def FullNm(self):
		return self._FullNm

	@FullNm.setter
	def FullNm(self, value):
		self._FullNm = value if type(value) != auto else self.make_default("FullNm")

	@FullNm.deleter
	def FullNm(self):
		del self._FullNm
		self._FullNm = None

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if type(value) != auto else self.make_default("Ctct")

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = None

	@property
	def SprvsgAuthrty(self):
		return self._SprvsgAuthrty

	@SprvsgAuthrty.setter
	def SprvsgAuthrty(self, value):
		self._SprvsgAuthrty = value if type(value) != auto else self.make_default("SprvsgAuthrty")

	@SprvsgAuthrty.deleter
	def SprvsgAuthrty(self):
		del self._SprvsgAuthrty
		self._SprvsgAuthrty = None

	@property
	def Cmnt(self):
		return self._Cmnt

	@Cmnt.setter
	def Cmnt(self, value):
		self._Cmnt = value if type(value) != auto else self.make_default("Cmnt")

	@Cmnt.deleter
	def Cmnt(self):
		del self._Cmnt
		self._Cmnt = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyTp', type=Max10Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctct', type=CommunicationAddress7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SprvsgAuthrty', type=SupervisingAuthorityIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmnt', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))

