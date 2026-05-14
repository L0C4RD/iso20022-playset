# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Document9 import Document9
from ._Max20000Text import Max20000Text
from ._Max2000Text import Max2000Text
from ._YesNoIndicator import YesNoIndicator

class DemandDocumentation1(base_types._BaseFieldType):

	__slots__ = ["_CmpltInd", "_CmpltnInf", "_DmndNrrtv", "_NclsdFile"]
	@property
	def CmpltInd(self):
		return self._CmpltInd

	@CmpltInd.setter
	def CmpltInd(self, value):
		self._CmpltInd = value if type(value) != base_types.auto else self.make_default("CmpltInd")

	@CmpltInd.deleter
	def CmpltInd(self):
		del self._CmpltInd
		self._CmpltInd = None

	@property
	def CmpltnInf(self):
		return self._CmpltnInf

	@CmpltnInf.setter
	def CmpltnInf(self, value):
		self._CmpltnInf = value if type(value) != base_types.auto else self.make_default("CmpltnInf")

	@CmpltnInf.deleter
	def CmpltnInf(self):
		del self._CmpltnInf
		self._CmpltnInf = None

	@property
	def DmndNrrtv(self):
		return self._DmndNrrtv

	@DmndNrrtv.setter
	def DmndNrrtv(self, value):
		self._DmndNrrtv = value if type(value) != base_types.auto else self.make_default("DmndNrrtv")

	@DmndNrrtv.deleter
	def DmndNrrtv(self):
		del self._DmndNrrtv
		self._DmndNrrtv = None

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if type(value) != base_types.auto else self.make_default("NclsdFile")

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmpltInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnInf', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndNrrtv', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document9, min=0, max=None, mutex_group=None, array=True),
	))