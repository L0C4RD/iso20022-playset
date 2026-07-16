# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Max2048Text
from . import Max256Text
from . import Max35Text
from . import Max70Text
from . import NamePrefix2Code
from . import OtherContact1
from . import PhoneNumber
from . import PreferredContactMethod2Code

class Contact13(base_types._BaseFieldType):

	__slots__ = ["_Dept", "_EmailAdr", "_EmailPurp", "_FaxNb", "_JobTitl", "_MobNb", "_Nm", "_NmPrfx", "_Othr", "_PhneNb", "_PrefrdMtd", "_Rspnsblty", "_URLAdr"]
	@property
	def Dept(self):
		return self._Dept

	@Dept.setter
	def Dept(self, value):
		self._Dept = value if value is not None else base_types.UninitialisedField(self, 'Dept', Max70Text, False)

	@Dept.deleter
	def Dept(self):
		del self._Dept
		self._Dept = base_types.UninitialisedField(self, 'Dept', Max70Text, False)

	@property
	def EmailAdr(self):
		return self._EmailAdr

	@EmailAdr.setter
	def EmailAdr(self, value):
		self._EmailAdr = value if value is not None else base_types.UninitialisedField(self, 'EmailAdr', Max256Text, False)

	@EmailAdr.deleter
	def EmailAdr(self):
		del self._EmailAdr
		self._EmailAdr = base_types.UninitialisedField(self, 'EmailAdr', Max256Text, False)

	@property
	def EmailPurp(self):
		return self._EmailPurp

	@EmailPurp.setter
	def EmailPurp(self, value):
		self._EmailPurp = value if value is not None else base_types.UninitialisedField(self, 'EmailPurp', Max35Text, False)

	@EmailPurp.deleter
	def EmailPurp(self):
		del self._EmailPurp
		self._EmailPurp = base_types.UninitialisedField(self, 'EmailPurp', Max35Text, False)

	@property
	def FaxNb(self):
		return self._FaxNb

	@FaxNb.setter
	def FaxNb(self, value):
		self._FaxNb = value if value is not None else base_types.UninitialisedField(self, 'FaxNb', PhoneNumber, False)

	@FaxNb.deleter
	def FaxNb(self):
		del self._FaxNb
		self._FaxNb = base_types.UninitialisedField(self, 'FaxNb', PhoneNumber, False)

	@property
	def JobTitl(self):
		return self._JobTitl

	@JobTitl.setter
	def JobTitl(self, value):
		self._JobTitl = value if value is not None else base_types.UninitialisedField(self, 'JobTitl', Max35Text, False)

	@JobTitl.deleter
	def JobTitl(self):
		del self._JobTitl
		self._JobTitl = base_types.UninitialisedField(self, 'JobTitl', Max35Text, False)

	@property
	def MobNb(self):
		return self._MobNb

	@MobNb.setter
	def MobNb(self, value):
		self._MobNb = value if value is not None else base_types.UninitialisedField(self, 'MobNb', PhoneNumber, False)

	@MobNb.deleter
	def MobNb(self):
		del self._MobNb
		self._MobNb = base_types.UninitialisedField(self, 'MobNb', PhoneNumber, False)

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
	def NmPrfx(self):
		return self._NmPrfx

	@NmPrfx.setter
	def NmPrfx(self, value):
		self._NmPrfx = value if value is not None else base_types.UninitialisedField(self, 'NmPrfx', NamePrefix2Code, False)

	@NmPrfx.deleter
	def NmPrfx(self):
		del self._NmPrfx
		self._NmPrfx = base_types.UninitialisedField(self, 'NmPrfx', NamePrefix2Code, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', OtherContact1, True)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', OtherContact1, True)

	@property
	def PhneNb(self):
		return self._PhneNb

	@PhneNb.setter
	def PhneNb(self, value):
		self._PhneNb = value if value is not None else base_types.UninitialisedField(self, 'PhneNb', PhoneNumber, False)

	@PhneNb.deleter
	def PhneNb(self):
		del self._PhneNb
		self._PhneNb = base_types.UninitialisedField(self, 'PhneNb', PhoneNumber, False)

	@property
	def PrefrdMtd(self):
		return self._PrefrdMtd

	@PrefrdMtd.setter
	def PrefrdMtd(self, value):
		self._PrefrdMtd = value if value is not None else base_types.UninitialisedField(self, 'PrefrdMtd', PreferredContactMethod2Code, False)

	@PrefrdMtd.deleter
	def PrefrdMtd(self):
		del self._PrefrdMtd
		self._PrefrdMtd = base_types.UninitialisedField(self, 'PrefrdMtd', PreferredContactMethod2Code, False)

	@property
	def Rspnsblty(self):
		return self._Rspnsblty

	@Rspnsblty.setter
	def Rspnsblty(self, value):
		self._Rspnsblty = value if value is not None else base_types.UninitialisedField(self, 'Rspnsblty', Max35Text, False)

	@Rspnsblty.deleter
	def Rspnsblty(self):
		del self._Rspnsblty
		self._Rspnsblty = base_types.UninitialisedField(self, 'Rspnsblty', Max35Text, False)

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if value is not None else base_types.UninitialisedField(self, 'URLAdr', Max2048Text, False)

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = base_types.UninitialisedField(self, 'URLAdr', Max2048Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dept', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EmailPurp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaxNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JobTitl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmPrfx', type=NamePrefix2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherContact1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PhneNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrefrdMtd', type=PreferredContactMethod2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspnsblty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
	))