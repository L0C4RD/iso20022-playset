# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._Max2048Text import Max2048Text
from ._TrueFalseIndicator import TrueFalseIndicator
from ._Visibilty1 import Visibilty1

class CreditorServiceEnrolment1(base_types._BaseFieldType):

	__slots__ = ["_CdtrSvcActvtnLk", "_EnrlmntEndDt", "_EnrlmntStartDt", "_SvcActvtnAllwd", "_SvcDescLk", "_Vsblty"]
	@property
	def CdtrSvcActvtnLk(self):
		return self._CdtrSvcActvtnLk

	@CdtrSvcActvtnLk.setter
	def CdtrSvcActvtnLk(self, value):
		self._CdtrSvcActvtnLk = value if type(value) != base_types.auto else self.make_default("CdtrSvcActvtnLk")

	@CdtrSvcActvtnLk.deleter
	def CdtrSvcActvtnLk(self):
		del self._CdtrSvcActvtnLk
		self._CdtrSvcActvtnLk = None

	@property
	def EnrlmntEndDt(self):
		return self._EnrlmntEndDt

	@EnrlmntEndDt.setter
	def EnrlmntEndDt(self, value):
		self._EnrlmntEndDt = value if type(value) != base_types.auto else self.make_default("EnrlmntEndDt")

	@EnrlmntEndDt.deleter
	def EnrlmntEndDt(self):
		del self._EnrlmntEndDt
		self._EnrlmntEndDt = None

	@property
	def EnrlmntStartDt(self):
		return self._EnrlmntStartDt

	@EnrlmntStartDt.setter
	def EnrlmntStartDt(self, value):
		self._EnrlmntStartDt = value if type(value) != base_types.auto else self.make_default("EnrlmntStartDt")

	@EnrlmntStartDt.deleter
	def EnrlmntStartDt(self):
		del self._EnrlmntStartDt
		self._EnrlmntStartDt = None

	@property
	def SvcActvtnAllwd(self):
		return self._SvcActvtnAllwd

	@SvcActvtnAllwd.setter
	def SvcActvtnAllwd(self, value):
		self._SvcActvtnAllwd = value if type(value) != base_types.auto else self.make_default("SvcActvtnAllwd")

	@SvcActvtnAllwd.deleter
	def SvcActvtnAllwd(self):
		del self._SvcActvtnAllwd
		self._SvcActvtnAllwd = None

	@property
	def SvcDescLk(self):
		return self._SvcDescLk

	@SvcDescLk.setter
	def SvcDescLk(self, value):
		self._SvcDescLk = value if type(value) != base_types.auto else self.make_default("SvcDescLk")

	@SvcDescLk.deleter
	def SvcDescLk(self):
		del self._SvcDescLk
		self._SvcDescLk = None

	@property
	def Vsblty(self):
		return self._Vsblty

	@Vsblty.setter
	def Vsblty(self, value):
		self._Vsblty = value if type(value) != base_types.auto else self.make_default("Vsblty")

	@Vsblty.deleter
	def Vsblty(self):
		del self._Vsblty
		self._Vsblty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtrSvcActvtnLk', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EnrlmntEndDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EnrlmntStartDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcActvtnAllwd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcDescLk', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vsblty', type=Visibilty1, min=0, max=1, mutex_group=None, array=False),
	))