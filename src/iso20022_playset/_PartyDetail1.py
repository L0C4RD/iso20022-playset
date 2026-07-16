# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationAddress7
from . import CountryCode
from . import Max10Text
from . import Max20000Text
from . import Max350Text
from . import PostalAddress6
from . import SupervisingAuthorityIdentification1Choice

class PartyDetail1(base_types._BaseFieldType):

	__slots__ = ["_Cmnt", "_Ctct", "_Ctry", "_FullNm", "_PstlAdr", "_PtyTp", "_SprvsgAuthrty"]
	@property
	def Cmnt(self):
		return self._Cmnt

	@Cmnt.setter
	def Cmnt(self, value):
		self._Cmnt = value if value is not None else base_types.UninitialisedField(self, 'Cmnt', Max20000Text, False)

	@Cmnt.deleter
	def Cmnt(self):
		del self._Cmnt
		self._Cmnt = base_types.UninitialisedField(self, 'Cmnt', Max20000Text, False)

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if value is not None else base_types.UninitialisedField(self, 'Ctct', CommunicationAddress7, False)

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = base_types.UninitialisedField(self, 'Ctct', CommunicationAddress7, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def FullNm(self):
		return self._FullNm

	@FullNm.setter
	def FullNm(self, value):
		self._FullNm = value if value is not None else base_types.UninitialisedField(self, 'FullNm', Max350Text, False)

	@FullNm.deleter
	def FullNm(self):
		del self._FullNm
		self._FullNm = base_types.UninitialisedField(self, 'FullNm', Max350Text, False)

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if value is not None else base_types.UninitialisedField(self, 'PstlAdr', PostalAddress6, False)

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = base_types.UninitialisedField(self, 'PstlAdr', PostalAddress6, False)

	@property
	def PtyTp(self):
		return self._PtyTp

	@PtyTp.setter
	def PtyTp(self, value):
		self._PtyTp = value if value is not None else base_types.UninitialisedField(self, 'PtyTp', Max10Text, False)

	@PtyTp.deleter
	def PtyTp(self):
		del self._PtyTp
		self._PtyTp = base_types.UninitialisedField(self, 'PtyTp', Max10Text, False)

	@property
	def SprvsgAuthrty(self):
		return self._SprvsgAuthrty

	@SprvsgAuthrty.setter
	def SprvsgAuthrty(self, value):
		self._SprvsgAuthrty = value if value is not None else base_types.UninitialisedField(self, 'SprvsgAuthrty', SupervisingAuthorityIdentification1Choice, False)

	@SprvsgAuthrty.deleter
	def SprvsgAuthrty(self):
		del self._SprvsgAuthrty
		self._SprvsgAuthrty = base_types.UninitialisedField(self, 'SprvsgAuthrty', SupervisingAuthorityIdentification1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmnt', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctct', type=CommunicationAddress7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyTp', type=Max10Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SprvsgAuthrty', type=SupervisingAuthorityIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
	))