# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthenticationChannel1Choice
from . import ISODate
from . import Max16Text

class MandateAuthentication1(base_types._BaseFieldType):

	__slots__ = ["_Chanl", "_Dt", "_MsgAuthntcnCd"]
	@property
	def Chanl(self):
		return self._Chanl

	@Chanl.setter
	def Chanl(self, value):
		self._Chanl = value if value is not None else base_types.UninitialisedField(self, 'Chanl', AuthenticationChannel1Choice, False)

	@Chanl.deleter
	def Chanl(self):
		del self._Chanl
		self._Chanl = base_types.UninitialisedField(self, 'Chanl', AuthenticationChannel1Choice, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def MsgAuthntcnCd(self):
		return self._MsgAuthntcnCd

	@MsgAuthntcnCd.setter
	def MsgAuthntcnCd(self, value):
		self._MsgAuthntcnCd = value if value is not None else base_types.UninitialisedField(self, 'MsgAuthntcnCd', Max16Text, False)

	@MsgAuthntcnCd.deleter
	def MsgAuthntcnCd(self):
		del self._MsgAuthntcnCd
		self._MsgAuthntcnCd = base_types.UninitialisedField(self, 'MsgAuthntcnCd', Max16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Chanl', type=AuthenticationChannel1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgAuthntcnCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
	))