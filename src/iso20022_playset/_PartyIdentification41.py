# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactDetails2
from . import CountryCode
from . import Max140Text
from . import Party8Choice
from . import PostalAddress6

class PartyIdentification41(base_types._BaseFieldType):

	__slots__ = ["_CtctDtls", "_CtryOfRes", "_Id", "_Nm", "_PstlAdr"]
	@property
	def CtctDtls(self):
		return self._CtctDtls

	@CtctDtls.setter
	def CtctDtls(self, value):
		self._CtctDtls = value if value is not None else base_types.UninitialisedField(self, 'CtctDtls', ContactDetails2, False)

	@CtctDtls.deleter
	def CtctDtls(self):
		del self._CtctDtls
		self._CtctDtls = base_types.UninitialisedField(self, 'CtctDtls', ContactDetails2, False)

	@property
	def CtryOfRes(self):
		return self._CtryOfRes

	@CtryOfRes.setter
	def CtryOfRes(self, value):
		self._CtryOfRes = value if value is not None else base_types.UninitialisedField(self, 'CtryOfRes', CountryCode, False)

	@CtryOfRes.deleter
	def CtryOfRes(self):
		del self._CtryOfRes
		self._CtryOfRes = base_types.UninitialisedField(self, 'CtryOfRes', CountryCode, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Party8Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Party8Choice, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max140Text, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctDtls', type=ContactDetails2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfRes', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Party8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress6, min=0, max=1, mutex_group=None, array=False),
	))