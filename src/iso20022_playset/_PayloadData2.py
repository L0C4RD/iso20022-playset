# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max35Text
from . import TrueFalseIndicator

class PayloadData2(base_types._BaseFieldType):

	__slots__ = ["_CreDtAndTm", "_PssblDplctFlg", "_PyldIdr"]
	@property
	def CreDtAndTm(self):
		return self._CreDtAndTm

	@CreDtAndTm.setter
	def CreDtAndTm(self, value):
		self._CreDtAndTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtAndTm', ISODateTime, False)

	@CreDtAndTm.deleter
	def CreDtAndTm(self):
		del self._CreDtAndTm
		self._CreDtAndTm = base_types.UninitialisedField(self, 'CreDtAndTm', ISODateTime, False)

	@property
	def PssblDplctFlg(self):
		return self._PssblDplctFlg

	@PssblDplctFlg.setter
	def PssblDplctFlg(self, value):
		self._PssblDplctFlg = value if value is not None else base_types.UninitialisedField(self, 'PssblDplctFlg', TrueFalseIndicator, False)

	@PssblDplctFlg.deleter
	def PssblDplctFlg(self):
		del self._PssblDplctFlg
		self._PssblDplctFlg = base_types.UninitialisedField(self, 'PssblDplctFlg', TrueFalseIndicator, False)

	@property
	def PyldIdr(self):
		return self._PyldIdr

	@PyldIdr.setter
	def PyldIdr(self, value):
		self._PyldIdr = value if value is not None else base_types.UninitialisedField(self, 'PyldIdr', Max35Text, False)

	@PyldIdr.deleter
	def PyldIdr(self):
		del self._PyldIdr
		self._PyldIdr = base_types.UninitialisedField(self, 'PyldIdr', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtAndTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PssblDplctFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PyldIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))