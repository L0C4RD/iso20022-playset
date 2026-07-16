# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenderCode
from . import ISODate
from . import Max35Text
from . import NamePrefix1Code
from . import PostalAddress1

class IndividualPerson8(base_types._BaseFieldType):

	__slots__ = ["_BirthDt", "_Gndr", "_GvnNm", "_IndvInvstrAdr", "_Nm", "_NmPrfx", "_NmSfx", "_SclSctyNb"]
	@property
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if value is not None else base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@property
	def Gndr(self):
		return self._Gndr

	@Gndr.setter
	def Gndr(self, value):
		self._Gndr = value if value is not None else base_types.UninitialisedField(self, 'Gndr', GenderCode, False)

	@Gndr.deleter
	def Gndr(self):
		del self._Gndr
		self._Gndr = base_types.UninitialisedField(self, 'Gndr', GenderCode, False)

	@property
	def GvnNm(self):
		return self._GvnNm

	@GvnNm.setter
	def GvnNm(self, value):
		self._GvnNm = value if value is not None else base_types.UninitialisedField(self, 'GvnNm', Max35Text, False)

	@GvnNm.deleter
	def GvnNm(self):
		del self._GvnNm
		self._GvnNm = base_types.UninitialisedField(self, 'GvnNm', Max35Text, False)

	@property
	def IndvInvstrAdr(self):
		return self._IndvInvstrAdr

	@IndvInvstrAdr.setter
	def IndvInvstrAdr(self, value):
		self._IndvInvstrAdr = value if value is not None else base_types.UninitialisedField(self, 'IndvInvstrAdr', PostalAddress1, False)

	@IndvInvstrAdr.deleter
	def IndvInvstrAdr(self):
		del self._IndvInvstrAdr
		self._IndvInvstrAdr = base_types.UninitialisedField(self, 'IndvInvstrAdr', PostalAddress1, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max35Text, False)

	@property
	def NmPrfx(self):
		return self._NmPrfx

	@NmPrfx.setter
	def NmPrfx(self, value):
		self._NmPrfx = value if value is not None else base_types.UninitialisedField(self, 'NmPrfx', NamePrefix1Code, False)

	@NmPrfx.deleter
	def NmPrfx(self):
		del self._NmPrfx
		self._NmPrfx = base_types.UninitialisedField(self, 'NmPrfx', NamePrefix1Code, False)

	@property
	def NmSfx(self):
		return self._NmSfx

	@NmSfx.setter
	def NmSfx(self, value):
		self._NmSfx = value if value is not None else base_types.UninitialisedField(self, 'NmSfx', Max35Text, False)

	@NmSfx.deleter
	def NmSfx(self):
		del self._NmSfx
		self._NmSfx = base_types.UninitialisedField(self, 'NmSfx', Max35Text, False)

	@property
	def SclSctyNb(self):
		return self._SclSctyNb

	@SclSctyNb.setter
	def SclSctyNb(self, value):
		self._SclSctyNb = value if value is not None else base_types.UninitialisedField(self, 'SclSctyNb', Max35Text, False)

	@SclSctyNb.deleter
	def SclSctyNb(self):
		del self._SclSctyNb
		self._SclSctyNb = base_types.UninitialisedField(self, 'SclSctyNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Gndr', type=GenderCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvInvstrAdr', type=PostalAddress1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmPrfx', type=NamePrefix1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmSfx', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SclSctyNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))