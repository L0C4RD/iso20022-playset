# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import YesNoIndicator

class AccountContract3(base_types._BaseFieldType):

	__slots__ = ["_ClsgDt", "_GoLiveDt", "_RmvlInd", "_TrgtClsgDt", "_TrgtGoLiveDt", "_UrgcyFlg"]
	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', ISODate, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', ISODate, False)

	@property
	def GoLiveDt(self):
		return self._GoLiveDt

	@GoLiveDt.setter
	def GoLiveDt(self, value):
		self._GoLiveDt = value if value is not None else base_types.UninitialisedField(self, 'GoLiveDt', ISODate, False)

	@GoLiveDt.deleter
	def GoLiveDt(self):
		del self._GoLiveDt
		self._GoLiveDt = base_types.UninitialisedField(self, 'GoLiveDt', ISODate, False)

	@property
	def RmvlInd(self):
		return self._RmvlInd

	@RmvlInd.setter
	def RmvlInd(self, value):
		self._RmvlInd = value if value is not None else base_types.UninitialisedField(self, 'RmvlInd', YesNoIndicator, False)

	@RmvlInd.deleter
	def RmvlInd(self):
		del self._RmvlInd
		self._RmvlInd = base_types.UninitialisedField(self, 'RmvlInd', YesNoIndicator, False)

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
		base_types.FieldEntry(name='ClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GoLiveDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmvlInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtGoLiveDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UrgcyFlg', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))