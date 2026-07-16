# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max210Text
from . import ReportItem1
from . import ReportItemRejectionReason1Choice

class ReportItemStatus1(base_types._BaseFieldType):

	__slots__ = ["_AddtlRsnInf", "_RptItm", "_Xcptn"]
	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlRsnInf', Max210Text, False)

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = base_types.UninitialisedField(self, 'AddtlRsnInf', Max210Text, False)

	@property
	def RptItm(self):
		return self._RptItm

	@RptItm.setter
	def RptItm(self, value):
		self._RptItm = value if value is not None else base_types.UninitialisedField(self, 'RptItm', ReportItem1, True)

	@RptItm.deleter
	def RptItm(self):
		del self._RptItm
		self._RptItm = base_types.UninitialisedField(self, 'RptItm', ReportItem1, True)

	@property
	def Xcptn(self):
		return self._Xcptn

	@Xcptn.setter
	def Xcptn(self, value):
		self._Xcptn = value if value is not None else base_types.UninitialisedField(self, 'Xcptn', ReportItemRejectionReason1Choice, False)

	@Xcptn.deleter
	def Xcptn(self):
		del self._Xcptn
		self._Xcptn = base_types.UninitialisedField(self, 'Xcptn', ReportItemRejectionReason1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRsnInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptItm', type=ReportItem1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Xcptn', type=ReportItemRejectionReason1Choice, min=1, max=1, mutex_group=None, array=False),
	))