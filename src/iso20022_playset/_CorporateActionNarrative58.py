# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2048Text
from . import Max350Text
from . import UpdatedURLlnformation6

class CorporateActionNarrative58(base_types._BaseFieldType):

	__slots__ = ["_EvtPrcgWebSiteAdr", "_NewCpnyNm", "_Offerr", "_URLAdr"]
	@property
	def EvtPrcgWebSiteAdr(self):
		return self._EvtPrcgWebSiteAdr

	@EvtPrcgWebSiteAdr.setter
	def EvtPrcgWebSiteAdr(self, value):
		self._EvtPrcgWebSiteAdr = value if value is not None else base_types.UninitialisedField(self, 'EvtPrcgWebSiteAdr', Max2048Text, False)

	@EvtPrcgWebSiteAdr.deleter
	def EvtPrcgWebSiteAdr(self):
		del self._EvtPrcgWebSiteAdr
		self._EvtPrcgWebSiteAdr = base_types.UninitialisedField(self, 'EvtPrcgWebSiteAdr', Max2048Text, False)

	@property
	def NewCpnyNm(self):
		return self._NewCpnyNm

	@NewCpnyNm.setter
	def NewCpnyNm(self, value):
		self._NewCpnyNm = value if value is not None else base_types.UninitialisedField(self, 'NewCpnyNm', Max350Text, False)

	@NewCpnyNm.deleter
	def NewCpnyNm(self):
		del self._NewCpnyNm
		self._NewCpnyNm = base_types.UninitialisedField(self, 'NewCpnyNm', Max350Text, False)

	@property
	def Offerr(self):
		return self._Offerr

	@Offerr.setter
	def Offerr(self, value):
		self._Offerr = value if value is not None else base_types.UninitialisedField(self, 'Offerr', Max350Text, True)

	@Offerr.deleter
	def Offerr(self):
		del self._Offerr
		self._Offerr = base_types.UninitialisedField(self, 'Offerr', Max350Text, True)

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if value is not None else base_types.UninitialisedField(self, 'URLAdr', UpdatedURLlnformation6, True)

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = base_types.UninitialisedField(self, 'URLAdr', UpdatedURLlnformation6, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtPrcgWebSiteAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewCpnyNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Offerr', type=Max350Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='URLAdr', type=UpdatedURLlnformation6, min=0, max=None, mutex_group=None, array=True),
	))