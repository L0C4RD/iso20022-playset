# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import Max2048Text
from . import TrueFalseIndicator
from . import Visibilty1

class CreditorServiceEnrolment1(base_types._BaseFieldType):

	__slots__ = ["_CdtrSvcActvtnLk", "_EnrlmntEndDt", "_EnrlmntStartDt", "_SvcActvtnAllwd", "_SvcDescLk", "_Vsblty"]
	@property
	def CdtrSvcActvtnLk(self):
		return self._CdtrSvcActvtnLk

	@CdtrSvcActvtnLk.setter
	def CdtrSvcActvtnLk(self, value):
		self._CdtrSvcActvtnLk = value if value is not None else base_types.UninitialisedField(self, 'CdtrSvcActvtnLk', Max2048Text, False)

	@CdtrSvcActvtnLk.deleter
	def CdtrSvcActvtnLk(self):
		del self._CdtrSvcActvtnLk
		self._CdtrSvcActvtnLk = base_types.UninitialisedField(self, 'CdtrSvcActvtnLk', Max2048Text, False)

	@property
	def EnrlmntEndDt(self):
		return self._EnrlmntEndDt

	@EnrlmntEndDt.setter
	def EnrlmntEndDt(self, value):
		self._EnrlmntEndDt = value if value is not None else base_types.UninitialisedField(self, 'EnrlmntEndDt', DateAndDateTime2Choice, False)

	@EnrlmntEndDt.deleter
	def EnrlmntEndDt(self):
		del self._EnrlmntEndDt
		self._EnrlmntEndDt = base_types.UninitialisedField(self, 'EnrlmntEndDt', DateAndDateTime2Choice, False)

	@property
	def EnrlmntStartDt(self):
		return self._EnrlmntStartDt

	@EnrlmntStartDt.setter
	def EnrlmntStartDt(self, value):
		self._EnrlmntStartDt = value if value is not None else base_types.UninitialisedField(self, 'EnrlmntStartDt', DateAndDateTime2Choice, False)

	@EnrlmntStartDt.deleter
	def EnrlmntStartDt(self):
		del self._EnrlmntStartDt
		self._EnrlmntStartDt = base_types.UninitialisedField(self, 'EnrlmntStartDt', DateAndDateTime2Choice, False)

	@property
	def SvcActvtnAllwd(self):
		return self._SvcActvtnAllwd

	@SvcActvtnAllwd.setter
	def SvcActvtnAllwd(self, value):
		self._SvcActvtnAllwd = value if value is not None else base_types.UninitialisedField(self, 'SvcActvtnAllwd', TrueFalseIndicator, False)

	@SvcActvtnAllwd.deleter
	def SvcActvtnAllwd(self):
		del self._SvcActvtnAllwd
		self._SvcActvtnAllwd = base_types.UninitialisedField(self, 'SvcActvtnAllwd', TrueFalseIndicator, False)

	@property
	def SvcDescLk(self):
		return self._SvcDescLk

	@SvcDescLk.setter
	def SvcDescLk(self, value):
		self._SvcDescLk = value if value is not None else base_types.UninitialisedField(self, 'SvcDescLk', Max2048Text, False)

	@SvcDescLk.deleter
	def SvcDescLk(self):
		del self._SvcDescLk
		self._SvcDescLk = base_types.UninitialisedField(self, 'SvcDescLk', Max2048Text, False)

	@property
	def Vsblty(self):
		return self._Vsblty

	@Vsblty.setter
	def Vsblty(self, value):
		self._Vsblty = value if value is not None else base_types.UninitialisedField(self, 'Vsblty', Visibilty1, False)

	@Vsblty.deleter
	def Vsblty(self):
		del self._Vsblty
		self._Vsblty = base_types.UninitialisedField(self, 'Vsblty', Visibilty1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtrSvcActvtnLk', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EnrlmntEndDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EnrlmntStartDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcActvtnAllwd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcDescLk', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vsblty', type=Visibilty1, min=0, max=1, mutex_group=None, array=False),
	))