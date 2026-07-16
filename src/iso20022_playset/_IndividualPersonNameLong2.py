# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max350Text
from . import Max35Text
from . import Max6Text
from . import NamePrefix2Code

class IndividualPersonNameLong2(base_types._BaseFieldType):

	__slots__ = ["_EndDt", "_GvnNm", "_Initls", "_MddlNm", "_Nm", "_NmPrfx", "_NmSfx", "_Srnm", "_StartDt"]
	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if value is not None else base_types.UninitialisedField(self, 'EndDt', ISODate, False)

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = base_types.UninitialisedField(self, 'EndDt', ISODate, False)

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
	def Initls(self):
		return self._Initls

	@Initls.setter
	def Initls(self, value):
		self._Initls = value if value is not None else base_types.UninitialisedField(self, 'Initls', Max6Text, False)

	@Initls.deleter
	def Initls(self):
		del self._Initls
		self._Initls = base_types.UninitialisedField(self, 'Initls', Max6Text, False)

	@property
	def MddlNm(self):
		return self._MddlNm

	@MddlNm.setter
	def MddlNm(self, value):
		self._MddlNm = value if value is not None else base_types.UninitialisedField(self, 'MddlNm', Max35Text, False)

	@MddlNm.deleter
	def MddlNm(self):
		del self._MddlNm
		self._MddlNm = base_types.UninitialisedField(self, 'MddlNm', Max35Text, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max350Text, False)

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
	def NmSfx(self):
		return self._NmSfx

	@NmSfx.setter
	def NmSfx(self, value):
		self._NmSfx = value if value is not None else base_types.UninitialisedField(self, 'NmSfx', Max350Text, False)

	@NmSfx.deleter
	def NmSfx(self):
		del self._NmSfx
		self._NmSfx = base_types.UninitialisedField(self, 'NmSfx', Max350Text, False)

	@property
	def Srnm(self):
		return self._Srnm

	@Srnm.setter
	def Srnm(self, value):
		self._Srnm = value if value is not None else base_types.UninitialisedField(self, 'Srnm', Max35Text, False)

	@Srnm.deleter
	def Srnm(self):
		del self._Srnm
		self._Srnm = base_types.UninitialisedField(self, 'Srnm', Max35Text, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Initls', type=Max6Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MddlNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmPrfx', type=NamePrefix2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmSfx', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Srnm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))