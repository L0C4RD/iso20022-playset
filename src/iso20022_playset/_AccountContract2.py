# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import YesNoIndicator

class AccountContract2(base_types._BaseFieldType):

	__slots__ = ["_TrgtClsgDt", "_TrgtGoLiveDt", "_UrgcyFlg"]
	@property
	def TrgtClsgDt(self):
		return self._TrgtClsgDt

	@TrgtClsgDt.setter
	def TrgtClsgDt(self, value):
		self._TrgtClsgDt = value if value is not None else base_types.UninitialisedField(self, 'TrgtClsgDt', ISODate, False)

	@TrgtClsgDt.deleter
	def TrgtClsgDt(self):
		del self._TrgtClsgDt
		self._TrgtClsgDt = base_types.UninitialisedField(self, 'TrgtClsgDt', ISODate, False)

	@property
	def TrgtGoLiveDt(self):
		return self._TrgtGoLiveDt

	@TrgtGoLiveDt.setter
	def TrgtGoLiveDt(self, value):
		self._TrgtGoLiveDt = value if value is not None else base_types.UninitialisedField(self, 'TrgtGoLiveDt', ISODate, False)

	@TrgtGoLiveDt.deleter
	def TrgtGoLiveDt(self):
		del self._TrgtGoLiveDt
		self._TrgtGoLiveDt = base_types.UninitialisedField(self, 'TrgtGoLiveDt', ISODate, False)

	@property
	def UrgcyFlg(self):
		return self._UrgcyFlg

	@UrgcyFlg.setter
	def UrgcyFlg(self, value):
		self._UrgcyFlg = value if value is not None else base_types.UninitialisedField(self, 'UrgcyFlg', YesNoIndicator, False)

	@UrgcyFlg.deleter
	def UrgcyFlg(self):
		del self._UrgcyFlg
		self._UrgcyFlg = base_types.UninitialisedField(self, 'UrgcyFlg', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrgtClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtGoLiveDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UrgcyFlg', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))