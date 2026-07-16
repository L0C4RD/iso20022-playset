# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTimeChoice
from . import Max2000Text
from . import Max35Text
from . import PartyIdentification43

class UndertakingConfirmation1(base_types._BaseFieldType):

	__slots__ = ["_Cnfrmr", "_Conf", "_Dt", "_RefNb"]
	@property
	def Cnfrmr(self):
		return self._Cnfrmr

	@Cnfrmr.setter
	def Cnfrmr(self, value):
		self._Cnfrmr = value if value is not None else base_types.UninitialisedField(self, 'Cnfrmr', PartyIdentification43, False)

	@Cnfrmr.deleter
	def Cnfrmr(self):
		del self._Cnfrmr
		self._Cnfrmr = base_types.UninitialisedField(self, 'Cnfrmr', PartyIdentification43, False)

	@property
	def Conf(self):
		return self._Conf

	@Conf.setter
	def Conf(self, value):
		self._Conf = value if value is not None else base_types.UninitialisedField(self, 'Conf', Max2000Text, True)

	@Conf.deleter
	def Conf(self):
		del self._Conf
		self._Conf = base_types.UninitialisedField(self, 'Conf', Max2000Text, True)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', DateAndDateTimeChoice, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', DateAndDateTimeChoice, False)

	@property
	def RefNb(self):
		return self._RefNb

	@RefNb.setter
	def RefNb(self, value):
		self._RefNb = value if value is not None else base_types.UninitialisedField(self, 'RefNb', Max35Text, False)

	@RefNb.deleter
	def RefNb(self):
		del self._RefNb
		self._RefNb = base_types.UninitialisedField(self, 'RefNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cnfrmr', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Conf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dt', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))