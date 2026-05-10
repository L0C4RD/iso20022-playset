from . import base_types
from .UpdatedURLlnformation6 import UpdatedURLlnformation6
from .Max350Text import Max350Text
from .Max2048Text import Max2048Text

class CorporateActionNarrative58(base_types._BaseFieldType):

	__slots__ = ["_Offerr", "_URLAdr", "_NewCpnyNm", "_EvtPrcgWebSiteAdr"]
	@property
	def Offerr(self):
		return self._Offerr

	@Offerr.setter
	def Offerr(self, value):
		self._Offerr = value if type(value) != auto else self.make_default("Offerr")

	@Offerr.deleter
	def Offerr(self):
		del self._Offerr
		self._Offerr = None

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if type(value) != auto else self.make_default("URLAdr")

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = None

	@property
	def NewCpnyNm(self):
		return self._NewCpnyNm

	@NewCpnyNm.setter
	def NewCpnyNm(self, value):
		self._NewCpnyNm = value if type(value) != auto else self.make_default("NewCpnyNm")

	@NewCpnyNm.deleter
	def NewCpnyNm(self):
		del self._NewCpnyNm
		self._NewCpnyNm = None

	@property
	def EvtPrcgWebSiteAdr(self):
		return self._EvtPrcgWebSiteAdr

	@EvtPrcgWebSiteAdr.setter
	def EvtPrcgWebSiteAdr(self, value):
		self._EvtPrcgWebSiteAdr = value if type(value) != auto else self.make_default("EvtPrcgWebSiteAdr")

	@EvtPrcgWebSiteAdr.deleter
	def EvtPrcgWebSiteAdr(self):
		del self._EvtPrcgWebSiteAdr
		self._EvtPrcgWebSiteAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Offerr', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='URLAdr', type=UpdatedURLlnformation6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewCpnyNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtPrcgWebSiteAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
	))

