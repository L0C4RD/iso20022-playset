# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4NumericText
from . import ISODate
from . import Max6AlphaText

class AgreementConditions1(base_types._BaseFieldType):

	__slots__ = ["_AgrmtCd", "_Dt", "_Vrsn"]
	@property
	def AgrmtCd(self):
		return self._AgrmtCd

	@AgrmtCd.setter
	def AgrmtCd(self, value):
		self._AgrmtCd = value if value is not None else base_types.UninitialisedField(self, 'AgrmtCd', Max6AlphaText, False)

	@AgrmtCd.deleter
	def AgrmtCd(self):
		del self._AgrmtCd
		self._AgrmtCd = base_types.UninitialisedField(self, 'AgrmtCd', Max6AlphaText, False)

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
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Exact4NumericText, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Exact4NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrmtCd', type=Max6AlphaText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Exact4NumericText, min=0, max=1, mutex_group=None, array=False),
	))